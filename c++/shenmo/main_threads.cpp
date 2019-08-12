#include <dirent.h>
#include <sys/types.h>
#include<time.h>
//////////////////////////////////////////////////////////////
#include <iostream>
#include <fstream>
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "gflags/gflags.h"
#include "gpu_sdk_export.h"
#include <sstream>
#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>
#include "rapidjson/document.h"
#include "rapidjson/filereadstream.h"
#include "rapidjson/filewritestream.h"
#include "rapidjson/prettywriter.h"
#include "rapidjson/stringbuffer.h"

using namespace std;
using namespace rapidjson;  //引入rapidjson命名空间                                                                                                                                                          

DEFINE_string(base_dir, "./shenmo-picture/", "base dir");
DEFINE_string(i, "./image.lst", "file name of image list");
DEFINE_string(sper, " ", "image.lst sperator (default space)");
DEFINE_int32(n, 1, "the num of image to prepared for test");
DEFINE_string(device, "0", "device id: 0,1,2");
DEFINE_string(thread_num, "1", "thread number of gpu. 8,9,10");
DEFINE_int32(f, 0, "the test function");
DEFINE_int32(b, 1, "the model network batch");
DEFINE_int32(auth_type, 2, "the type of auth 1:local 2:net");
DEFINE_string(auth_server, "192.168.1.198:12821", "the port of the server to listen");
DEFINE_string(param_file, "./shenmo-pictuire/centos7/bin/param.txt", "param.txt used by recognize.");


int test_work_batch(const std::vector<std::string>& image_list, const std::vector<std::string>& output_list, int device, int batch);

template <typename T>
std::string num2str(const T i){
    std::stringstream stream;
    stream << i;
    return stream.str();
}

std::vector<std::string> split(const std::string &s, const std::string &seperator){
    std::vector<std::string> result;
    typedef std::string::size_type string_size;
    string_size i = 0;

    while(i != s.size()){
        //找到字符串中首个不等于分隔符的字母；
        int flag = 0;
        while(i != s.size() && flag == 0){
            flag = 1;
            for(string_size x = 0; x < seperator.size(); ++x)
                if(s[i] == seperator[x]){
                    ++i;
                    flag = 0;
                    break;
                }
        }

        //找到又一个分隔符，将两个分隔符之间的字符串取出；
        flag = 0;
        string_size j = i;
        while(j != s.size() && flag == 0){
            for(string_size x = 0; x < seperator.size(); ++x)
                if(s[j] == seperator[x]){
                    flag = 1;
                    break;
                }
            if(flag == 0)
                ++j;
        }
        if(i != j){
            result.push_back(s.substr(i, j-i));
            i = j;
        }
    }
    return result;
}
std::string get_upload_time(time_t t = 0){
    if (!t){
        t = time(NULL);
    }

    struct tm *tm = localtime(&t);
    // yyyy-mm-dd hh:mm:ss
    char buf[128] = {0};
    sprintf(buf, "%4d-%.2d-%.2d %.2d:%.2d:%.2d",tm->tm_year+1900,tm->tm_mon+1,tm->tm_mday, tm->tm_hour,tm->tm_min,tm->tm_sec);

    return buf;
}


static std::string json_param = "";
std::vector<std::string> vfilename;
std::vector<std::string> output_file;
std::vector<int> vec_device;
std::vector<int> vec_thread_num;

struct thread_info{
    int device;
    int batch_num;
    std::vector<std::string>* img_vec;
    std::vector<std::string>* img_output_vec;
};

void printids(const char *s){
    pid_t pid;
    pthread_t tid;
  
    pid = getpid();
    tid = pthread_self();
    printf("%s pid %u tid %u (0x%x)\n", s, (unsigned int)pid, (unsigned int)tid,(unsigned int)tid);
}

void* thr_fn(void* arg){
    printids("new thread: ");
    thread_info* tinfo = (thread_info*)arg;
    if (NULL == tinfo){
        return ((void*)0);
    }
	printf("pic number=[%d]device=[%d]batch_name=[%d]\n", tinfo->img_vec->size(), tinfo->device, tinfo->batch_num);
    std::cout << "pic number = " << tinfo->img_vec->size()<< "device=["<< tinfo->device<< "]batch_name=["<< tinfo->batch_num <<"]" <<std::endl;

	test_work_batch(*(tinfo->img_vec), *(tinfo->img_output_vec), tinfo->device, tinfo->batch_num);

    return ((void*)0);
}

void create_one_thread(pthread_t* t_id,thread_info* tinfo)
{
    int err;
    err = pthread_create(t_id, NULL, thr_fn, tinfo);
    if (err != 0){
        printf("can't create thread: %s\n", strerror(err));
    }

}

void create_all_thread(std::vector<std::string>& image_vec,std::vector<std::string>& image_output_vec){

    int i = 0;
    int num = 0;
	for (int i = 0; i < vec_thread_num.size(); i++){
		num += vec_thread_num[i];
	}
	cout << "image size=" << image_vec.size() << endl;
    std::vector<std::string>* p_img_vec = new std::vector<std::string>[num];
    std::vector<std::string>* p_img_output_vec = new std::vector<std::string>[num];
    for(i = 0; i < image_vec.size(); i++){
        p_img_vec[i%num].push_back(image_vec[i]);
        p_img_output_vec[i%num].push_back(image_output_vec[i]);
    }

    pthread_t* pth_arr = new pthread_t[num]();
    thread_info* p_tinfo_arr = new thread_info[num]();
  
    // init
    int thread_count = 0;
    for (i = 0; i < vec_device.size(); i ++){
		int thread_num = vec_thread_num[i];
		for (int j = 0; j < thread_num; j++){
			p_tinfo_arr[thread_count].device = vec_device[i];
			p_tinfo_arr[thread_count].batch_num = FLAGS_n;
			p_tinfo_arr[thread_count].img_vec = p_img_vec+thread_count;
			p_tinfo_arr[thread_count].img_output_vec = p_img_output_vec+thread_count;
			thread_count++;
		}
    }

    for (i = 0;i < num; i++){
        create_one_thread(&pth_arr[i], &p_tinfo_arr[i]);
    }

    for (i = 0;i < num; i++){
        int err = pthread_join(pth_arr[i], NULL);
        if (0 != err){
            printf("can't join with thread %x", pth_arr[i]);
        }
    }
    delete [] p_tinfo_arr;
    delete [] pth_arr;
    delete [] p_img_vec;
}


void filescan_lst(const char *path, std::string sper, std::vector<std::string>& vec_file, std::vector<std::string>& vec_output)
{
    if (!path){
        perror("path is null");
    }
    std::fstream f(path);//创建一个fstream文件流对象
    std::string line;
    while (getline(f, line)){
        std::vector<std::string> vec = split(line, sper);
        vec_file.push_back(vec[0]);
        vec_output.push_back(vec[1]);
    }
}


void write_file(std::string& filename, char* buffer){
	FILE * fp = fopen(filename.c_str(), "wb");
	if (fp) {
		fwrite(buffer, strlen(buffer), 1, fp);
		fclose(fp);
	}
}
void append_file(std::string& filename, char* buffer){
	FILE * fp = fopen(filename.c_str(), "ab");
	if (fp) {
		fwrite(buffer, strlen(buffer), 1, fp);
		fclose(fp);
	}
}

int load_binary(const std::string& file, std::string& content, const char* fmode="r")
{
    
	content.clear();
	FILE* fp = fopen(file.c_str(), fmode);
	if (NULL == fp) {
		std::cout << "can't open " << file << std::endl;
		return -1;
	}
	fseek(fp, 0, SEEK_END);
	int tmp_len = ftell(fp);

	if (0 == tmp_len) {
		std::cout << file << " is empty" << std::endl;
		fclose(fp);
		return -1;
	}
	fseek(fp, 0, SEEK_SET);
	content.resize(tmp_len, 0);
	char* pcontent = const_cast<char*>(content.c_str());
	tmp_len == fread(pcontent, 1, tmp_len, fp);
	fclose(fp);

	return 0;
}

bool split_ImageResults(const char* json, std::vector<std::string>& vec_name)
{
    Document doc;
    if (doc.Parse(json).HasParseError()){
        cout << "parse error!" << endl;
        return false;
    }
    int code = doc["Code"].GetInt();
    std::string message = doc["Message"].GetString();

    Value &image_arr=doc["ImageResults"];
    int size = (int)image_arr.Size();
    if (size != vec_name.size()){
        cout << "image 识别张数不对 size=[" <<  size<< "]vec_name.size=[" << vec_name.size() << "]" << endl;
        for (int i = 0; i < vec_name.size(); i++){
            cout << vec_name[i] << endl;
        }
        return false;
    }
    for (int i = 0; i < size; i++){
        Value& e = image_arr[i];

        Document doc1;
        doc1.SetObject();
        Document::AllocatorType &allocator=doc1.GetAllocator(); //获取分配器                                                                                                                                 
        Value ImageResults(kArrayType);
        ImageResults.PushBack(e, allocator);
        Value Message(kStringType);
        Message.SetString(message.c_str(), allocator);

        doc1.AddMember("Code", code, allocator);
        doc1.AddMember("Message", Message, allocator);
        doc1.AddMember("ImageResults", ImageResults, allocator);

        StringBuffer buffer;
        PrettyWriter<StringBuffer> pretty_writer(buffer);  //PrettyWriter是格式化的json，如果是Writer则是换行空格压缩后的json
        doc1.Accept(pretty_writer);
        std::string  str = buffer.GetString();
        write_file(vec_name[i], const_cast<char*>(str.c_str()));
    }

    return true;
}



int test_work_batch(const std::vector<std::string>& image_list, const std::vector<std::string>& output_list, int device, int batch)
{
	int size = image_list.size();
	if (size < batch) {
		std::cout << "not enough photos for batch size " << FLAGS_n << " in this dir" << std::endl;
		return -1;
	}

	seemmo_thread_init(3, device, batch);
	// test imdecode
	unsigned char **ppbuf = new unsigned char* [batch];
	std::vector<cv::Mat> mats(batch);
	int *pheight = new int[batch];
	int *pwidth = new int[batch];
	int *chns  = new int[batch];
	int *timestamps = new int[batch];
	int total = 0;
	int recog_count = 0;

	for (int num = 0; num < size/batch; num++){
			
		std::vector<std::vector<unsigned char>* > image_data_list;
		std::vector<std::string> vec_filename;
		image_data_list.resize(batch);
		for (int i = 0; i < batch; ++i) {
			std::string img_data;
			std::string filename = image_list[recog_count];
            std::string output_name = output_list[recog_count];
            recog_count ++;
			if (0 != load_binary(filename, img_data, "rb")) {
				continue;	
			}
			image_data_list[i] = new std::vector<unsigned char>(img_data.begin(), img_data.end());
			if(NULL == image_data_list[i]){
				std::cout << "new image data failed" << std::endl;
				continue;
			}
            
			vec_filename.push_back(output_name);
            std::string name = num2str<pthread_t>(pthread_self());
			filename += "\n";
			append_file(name,const_cast<char*>(filename.c_str()));

		}

		std::vector<const char* > params;

		for (int i = 0; i < batch; ++i) {
			mats[i] = cv::imdecode(*image_data_list[i], 1);
			ppbuf[i] = mats[i].data; 
			pheight[i] = mats[i].rows;
			pwidth[i] = mats[i].cols;
			chns[i] = 0;
			timestamps[i] = i + 1;
			params.push_back(json_param.c_str());
		}
		clock_t start = clock();
		int buff_len = 1024 * 1024 * 8;
		char *res_buf = new char[buff_len];
		int ret = 0;
		if (0 == FLAGS_f) {
			ret = seemmo_recog_images((const uint8_t **)ppbuf, batch, (const uint32_t *)pheight, (const uint32_t *)pwidth, params.data(), res_buf, buff_len, 2);
		} 
		clock_t one_time = (clock() - start)*999997.0/CLOCKS_PER_SEC;
		total += one_time;

		//if (0 == FLAGS_f)
        //save_result("batch_res",res_buf);
		std::cout << "batch = "<< batch << " time=: " << one_time/1000.0<< "ms" << std::endl;

		if (res_buf){
			std::string name = "output.txt";	
			write_file(name, res_buf);
			split_ImageResults(res_buf, vec_filename);
			delete res_buf;
		}

		for (int i = 0; i < image_data_list.size(); i++){
			if (image_data_list[i]) delete image_data_list[i];
		}
	}	
	seemmo_thread_uninit();

	std::cout << "count=: " << size/(total/1000000.0)<< "s" << std::endl;
}

int main(int argc, char** argv)
{
    google::ParseCommandLineFlags(&argc, &argv, true);	
    // init
    clock_t start = clock();
    std::cout << "Test..." << std::endl;
	std::string str = FLAGS_device;
	std::string sper = ",";
	std::vector<std::string> vec = split(str, sper);
	for (int i = 0; i < vec.size(); i++){
		vec_device.push_back(atoi(vec[i].c_str()));
	}
	
	str = FLAGS_thread_num;
	vec = split(str, sper);
	for (int i = 0; i < vec.size(); i++){
		vec_thread_num.push_back(atoi(vec[i].c_str()));
	}

	for (int i = 0; i < vec_device.size(); i++){
		cout << "device=" << vec_device[i] << ", thread_num=" << vec_thread_num[i] << endl;
	}
    int image_core = 0;
	for (int i = 0; i < vec_thread_num.size(); i++){
		image_core += vec_thread_num[i];
	}
	int ret = seemmo_process_init(FLAGS_base_dir.c_str(), image_core, image_core, FLAGS_auth_server.c_str(), FLAGS_auth_type, true);
	std::cout << "Initialize SDK: " << ret << std::endl;
    
	// json param
	std::ifstream  in;
	in.open(FLAGS_param_file.c_str());
    std::cout << "json_param=[" << FLAGS_param_file.c_str() << "]" <<  std::endl;
	if (in.is_open()){
		char strtemp[1024 * 10] = { '\0' };
		in.read(strtemp, 1024 * 10);
        std::cout << "json_param=[" << json_param << "]" <<  std::endl;
		json_param = strtemp;
	}
	
	std::cout << "json_param=[" << json_param << "]" <<  std::endl;
    filescan_lst(FLAGS_i.c_str(), FLAGS_sper,vfilename, output_file);    

    // exec
    create_all_thread(vfilename, output_file);
    // exit
    ret = seemmo_uninit();
    std::cout << "unInitialize SDK: " << ret << std::endl;
    clock_t total = (clock() - start)*999997.0/CLOCKS_PER_SEC;
    std::cout << "total file= " << vfilename.size()<< std::endl;
    std::cout << "total time= " << total << std::endl;
    return 0;
}
