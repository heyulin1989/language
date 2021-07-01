00000000000b7dc0 <memcpy@GLIBC_2.2.5>:
   b7dc0:	f3 0f 1e fa          	endbr64 
   b7dc4:	48 89 f8             	mov    rax,rdi
   b7dc7:	48 83 fa 10          	cmp    rdx,0x10
   b7dcb:	0f 82 1a 01 00 00    	jb     b7eeb <memcpy@GLIBC_2.2.5+0x12b>
   b7dd1:	48 83 fa 20          	cmp    rdx,0x20
   b7dd5:	0f 87 5f 01 00 00    	ja     b7f3a <memcpy@GLIBC_2.2.5+0x17a>
   b7ddb:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b7dde:	0f 10 4c 16 f0       	movups xmm1,XMMWORD PTR [rsi+rdx*1-0x10]
   b7de3:	0f 11 07             	movups XMMWORD PTR [rdi],xmm0
   b7de6:	0f 11 4c 17 f0       	movups XMMWORD PTR [rdi+rdx*1-0x10],xmm1
   b7deb:	c3                   	ret    
   b7dec:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
   b7df0:	f3 0f 1e fa          	endbr64 
   b7df4:	48 39 d1             	cmp    rcx,rdx
   b7df7:	0f 82 23 02 07 00    	jb     128020 <__chk_fail@@GLIBC_2.3.4>
   b7dfd:	0f 1f 00             	nop    DWORD PTR [rax]
   b7e00:	f3 0f 1e fa          	endbr64 
   b7e04:	48 89 f8             	mov    rax,rdi
   b7e07:	48 85 d2             	test   rdx,rdx
   b7e0a:	74 45                	je     b7e51 <memcpy@GLIBC_2.2.5+0x91>
   b7e0c:	48 01 d0             	add    rax,rdx
   b7e0f:	eb 2b                	jmp    b7e3c <memcpy@GLIBC_2.2.5+0x7c>
   b7e11:	66 66 2e 0f 1f 84 00 	data16 nop WORD PTR cs:[rax+rax*1+0x0]
   b7e18:	00 00 00 00 
   b7e1c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
   b7e20:	f3 0f 1e fa          	endbr64 
   b7e24:	48 39 d1             	cmp    rcx,rdx
   b7e27:	0f 82 f3 01 07 00    	jb     128020 <__chk_fail@@GLIBC_2.3.4>
   b7e2d:	0f 1f 00             	nop    DWORD PTR [rax]
   b7e30:	f3 0f 1e fa          	endbr64 
   b7e34:	48 89 f8             	mov    rax,rdi
   b7e37:	48 85 d2             	test   rdx,rdx
   b7e3a:	74 15                	je     b7e51 <memcpy@GLIBC_2.2.5+0x91>
   b7e3c:	48 89 d1             	mov    rcx,rdx
   b7e3f:	48 39 f7             	cmp    rdi,rsi
   b7e42:	72 0b                	jb     b7e4f <memcpy@GLIBC_2.2.5+0x8f>
   b7e44:	74 0b                	je     b7e51 <memcpy@GLIBC_2.2.5+0x91>
   b7e46:	48 8d 14 0e          	lea    rdx,[rsi+rcx*1]
   b7e4a:	48 39 d7             	cmp    rdi,rdx
   b7e4d:	72 03                	jb     b7e52 <memcpy@GLIBC_2.2.5+0x92>
   b7e4f:	f3 a4                	rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
   b7e51:	c3                   	ret    
   b7e52:	48 8d 7c 0f ff       	lea    rdi,[rdi+rcx*1-0x1]
   b7e57:	48 8d 74 0e ff       	lea    rsi,[rsi+rcx*1-0x1]
   b7e5c:	fd                   	std    
   b7e5d:	f3 a4                	rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
   b7e5f:	fc                   	cld    
   b7e60:	c3                   	ret    
   b7e61:	66 66 2e 0f 1f 84 00 	data16 nop WORD PTR cs:[rax+rax*1+0x0]
   b7e68:	00 00 00 00 
   b7e6c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
   b7e70:	f3 0f 1e fa          	endbr64 
   b7e74:	48 39 d1             	cmp    rcx,rdx
   b7e77:	0f 82 a3 01 07 00    	jb     128020 <__chk_fail@@GLIBC_2.3.4>
   b7e7d:	0f 1f 00             	nop    DWORD PTR [rax]
   b7e80:	f3 0f 1e fa          	endbr64 
   b7e84:	48 89 f8             	mov    rax,rdi
   b7e87:	48 01 d0             	add    rax,rdx
   b7e8a:	eb 1b                	jmp    b7ea7 <memcpy@GLIBC_2.2.5+0xe7>
   b7e8c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
   b7e90:	f3 0f 1e fa          	endbr64 
   b7e94:	48 39 d1             	cmp    rcx,rdx
   b7e97:	0f 82 83 01 07 00    	jb     128020 <__chk_fail@@GLIBC_2.3.4>
   b7e9d:	0f 1f 00             	nop    DWORD PTR [rax]
   b7ea0:	f3 0f 1e fa          	endbr64 
   b7ea4:	48 89 f8             	mov    rax,rdi
   b7ea7:	48 83 fa 10          	cmp    rdx,0x10
   b7eab:	72 3e                	jb     b7eeb <memcpy@GLIBC_2.2.5+0x12b>
   b7ead:	48 83 fa 20          	cmp    rdx,0x20
   b7eb1:	77 7e                	ja     b7f31 <memcpy@GLIBC_2.2.5+0x171>
   b7eb3:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b7eb6:	0f 10 4c 16 f0       	movups xmm1,XMMWORD PTR [rsi+rdx*1-0x10]
   b7ebb:	0f 11 07             	movups XMMWORD PTR [rdi],xmm0
   b7ebe:	0f 11 4c 17 f0       	movups XMMWORD PTR [rdi+rdx*1-0x10],xmm1
   b7ec3:	c3                   	ret    
   b7ec4:	48 3b 15 cd f0 12 00 	cmp    rdx,QWORD PTR [rip+0x12f0cd]        # 1e6f98 <_obstack@GLIBC_2.2.5+0x80>
   b7ecb:	0f 83 e2 00 00 00    	jae    b7fb3 <memcpy@GLIBC_2.2.5+0x1f3>
   b7ed1:	48 39 f7             	cmp    rdi,rsi
   b7ed4:	72 0f                	jb     b7ee5 <memcpy@GLIBC_2.2.5+0x125>
   b7ed6:	74 12                	je     b7eea <memcpy@GLIBC_2.2.5+0x12a>
   b7ed8:	4c 8d 0c 16          	lea    r9,[rsi+rdx*1]
   b7edc:	4c 39 cf             	cmp    rdi,r9
   b7edf:	0f 82 63 01 00 00    	jb     b8048 <memcpy@GLIBC_2.2.5+0x288>
   b7ee5:	48 89 d1             	mov    rcx,rdx
   b7ee8:	f3 a4                	rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]
   b7eea:	c3                   	ret    
   b7eeb:	80 fa 08             	cmp    dl,0x8
   b7eee:	73 12                	jae    b7f02 <memcpy@GLIBC_2.2.5+0x142>
   b7ef0:	80 fa 04             	cmp    dl,0x4
   b7ef3:	73 1e                	jae    b7f13 <memcpy@GLIBC_2.2.5+0x153>
   b7ef5:	80 fa 01             	cmp    dl,0x1
   b7ef8:	77 26                	ja     b7f20 <memcpy@GLIBC_2.2.5+0x160>
   b7efa:	72 05                	jb     b7f01 <memcpy@GLIBC_2.2.5+0x141>
   b7efc:	0f b6 0e             	movzx  ecx,BYTE PTR [rsi]
   b7eff:	88 0f                	mov    BYTE PTR [rdi],cl
   b7f01:	c3                   	ret    
   b7f02:	48 8b 4c 16 f8       	mov    rcx,QWORD PTR [rsi+rdx*1-0x8]
   b7f07:	48 8b 36             	mov    rsi,QWORD PTR [rsi]
   b7f0a:	48 89 4c 17 f8       	mov    QWORD PTR [rdi+rdx*1-0x8],rcx
   b7f0f:	48 89 37             	mov    QWORD PTR [rdi],rsi
   b7f12:	c3                   	ret    
   b7f13:	8b 4c 16 fc          	mov    ecx,DWORD PTR [rsi+rdx*1-0x4]
   b7f17:	8b 36                	mov    esi,DWORD PTR [rsi]
   b7f19:	89 4c 17 fc          	mov    DWORD PTR [rdi+rdx*1-0x4],ecx
   b7f1d:	89 37                	mov    DWORD PTR [rdi],esi
   b7f1f:	c3                   	ret    
   b7f20:	0f b7 4c 16 fe       	movzx  ecx,WORD PTR [rsi+rdx*1-0x2]
   b7f25:	0f b7 36             	movzx  esi,WORD PTR [rsi]
   b7f28:	66 89 4c 17 fe       	mov    WORD PTR [rdi+rdx*1-0x2],cx
   b7f2d:	66 89 37             	mov    WORD PTR [rdi],si
   b7f30:	c3                   	ret    
   b7f31:	48 3b 15 c8 b3 12 00 	cmp    rdx,QWORD PTR [rip+0x12b3c8]        # 1e3300 <obstack_exit_failure@@GLIBC_2.2.5+0x10>
   b7f38:	77 8a                	ja     b7ec4 <memcpy@GLIBC_2.2.5+0x104>
   b7f3a:	48 81 fa 80 00 00 00 	cmp    rdx,0x80
   b7f41:	77 70                	ja     b7fb3 <memcpy@GLIBC_2.2.5+0x1f3>
   b7f43:	48 83 fa 40          	cmp    rdx,0x40
   b7f47:	72 47                	jb     b7f90 <memcpy@GLIBC_2.2.5+0x1d0>
   b7f49:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b7f4c:	0f 10 4e 10          	movups xmm1,XMMWORD PTR [rsi+0x10]
   b7f50:	0f 10 56 20          	movups xmm2,XMMWORD PTR [rsi+0x20]
   b7f54:	0f 10 5e 30          	movups xmm3,XMMWORD PTR [rsi+0x30]
   b7f58:	0f 10 64 16 f0       	movups xmm4,XMMWORD PTR [rsi+rdx*1-0x10]
   b7f5d:	0f 10 6c 16 e0       	movups xmm5,XMMWORD PTR [rsi+rdx*1-0x20]
   b7f62:	0f 10 74 16 d0       	movups xmm6,XMMWORD PTR [rsi+rdx*1-0x30]
   b7f67:	0f 10 7c 16 c0       	movups xmm7,XMMWORD PTR [rsi+rdx*1-0x40]
   b7f6c:	0f 11 07             	movups XMMWORD PTR [rdi],xmm0
   b7f6f:	0f 11 4f 10          	movups XMMWORD PTR [rdi+0x10],xmm1
   b7f73:	0f 11 57 20          	movups XMMWORD PTR [rdi+0x20],xmm2
   b7f77:	0f 11 5f 30          	movups XMMWORD PTR [rdi+0x30],xmm3
   b7f7b:	0f 11 64 17 f0       	movups XMMWORD PTR [rdi+rdx*1-0x10],xmm4
   b7f80:	0f 11 6c 17 e0       	movups XMMWORD PTR [rdi+rdx*1-0x20],xmm5
   b7f85:	0f 11 74 17 d0       	movups XMMWORD PTR [rdi+rdx*1-0x30],xmm6
   b7f8a:	0f 11 7c 17 c0       	movups XMMWORD PTR [rdi+rdx*1-0x40],xmm7
   b7f8f:	c3                   	ret    
   b7f90:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b7f93:	0f 10 4e 10          	movups xmm1,XMMWORD PTR [rsi+0x10]
   b7f97:	0f 10 54 16 f0       	movups xmm2,XMMWORD PTR [rsi+rdx*1-0x10]
   b7f9c:	0f 10 5c 16 e0       	movups xmm3,XMMWORD PTR [rsi+rdx*1-0x20]
   b7fa1:	0f 11 07             	movups XMMWORD PTR [rdi],xmm0
   b7fa4:	0f 11 4f 10          	movups XMMWORD PTR [rdi+0x10],xmm1
   b7fa8:	0f 11 54 17 f0       	movups XMMWORD PTR [rdi+rdx*1-0x10],xmm2
   b7fad:	0f 11 5c 17 e0       	movups XMMWORD PTR [rdi+rdx*1-0x20],xmm3
   b7fb2:	c3                   	ret    
   b7fb3:	48 39 f7             	cmp    rdi,rsi
   b7fb6:	0f 87 8c 00 00 00    	ja     b8048 <memcpy@GLIBC_2.2.5+0x288>
   b7fbc:	0f 84 28 ff ff ff    	je     b7eea <memcpy@GLIBC_2.2.5+0x12a>
   b7fc2:	0f 10 26             	movups xmm4,XMMWORD PTR [rsi]
   b7fc5:	0f 10 6c 16 f0       	movups xmm5,XMMWORD PTR [rsi+rdx*1-0x10]
   b7fca:	0f 10 74 16 e0       	movups xmm6,XMMWORD PTR [rsi+rdx*1-0x20]
   b7fcf:	0f 10 7c 16 d0       	movups xmm7,XMMWORD PTR [rsi+rdx*1-0x30]
   b7fd4:	44 0f 10 44 16 c0    	movups xmm8,XMMWORD PTR [rsi+rdx*1-0x40]
   b7fda:	49 89 fb             	mov    r11,rdi
   b7fdd:	48 8d 4c 17 f0       	lea    rcx,[rdi+rdx*1-0x10]
   b7fe2:	49 89 f8             	mov    r8,rdi
   b7fe5:	49 83 e0 0f          	and    r8,0xf
   b7fe9:	49 83 e8 10          	sub    r8,0x10
   b7fed:	4c 29 c6             	sub    rsi,r8
   b7ff0:	4c 29 c7             	sub    rdi,r8
   b7ff3:	4c 01 c2             	add    rdx,r8
   b7ff6:	48 3b 15 9b ef 12 00 	cmp    rdx,QWORD PTR [rip+0x12ef9b]        # 1e6f98 <_obstack@GLIBC_2.2.5+0x80>
   b7ffd:	0f 87 cc 00 00 00    	ja     b80cf <memcpy@GLIBC_2.2.5+0x30f>
   b8003:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b8006:	0f 10 4e 10          	movups xmm1,XMMWORD PTR [rsi+0x10]
   b800a:	0f 10 56 20          	movups xmm2,XMMWORD PTR [rsi+0x20]
   b800e:	0f 10 5e 30          	movups xmm3,XMMWORD PTR [rsi+0x30]
   b8012:	48 83 c6 40          	add    rsi,0x40
   b8016:	48 83 ea 40          	sub    rdx,0x40
   b801a:	0f 29 07             	movaps XMMWORD PTR [rdi],xmm0
   b801d:	0f 29 4f 10          	movaps XMMWORD PTR [rdi+0x10],xmm1
   b8021:	0f 29 57 20          	movaps XMMWORD PTR [rdi+0x20],xmm2
   b8025:	0f 29 5f 30          	movaps XMMWORD PTR [rdi+0x30],xmm3
   b8029:	48 83 c7 40          	add    rdi,0x40
   b802d:	48 83 fa 40          	cmp    rdx,0x40
   b8031:	77 d0                	ja     b8003 <memcpy@GLIBC_2.2.5+0x243>
   b8033:	0f 11 29             	movups XMMWORD PTR [rcx],xmm5
   b8036:	0f 11 71 f0          	movups XMMWORD PTR [rcx-0x10],xmm6
   b803a:	0f 11 79 e0          	movups XMMWORD PTR [rcx-0x20],xmm7
   b803e:	44 0f 11 41 d0       	movups XMMWORD PTR [rcx-0x30],xmm8
   b8043:	41 0f 11 23          	movups XMMWORD PTR [r11],xmm4
   b8047:	c3                   	ret    
   b8048:	0f 10 26             	movups xmm4,XMMWORD PTR [rsi]
   b804b:	0f 10 6e 10          	movups xmm5,XMMWORD PTR [rsi+0x10]
   b804f:	0f 10 76 20          	movups xmm6,XMMWORD PTR [rsi+0x20]
   b8053:	0f 10 7e 30          	movups xmm7,XMMWORD PTR [rsi+0x30]
   b8057:	44 0f 10 44 16 f0    	movups xmm8,XMMWORD PTR [rsi+rdx*1-0x10]
   b805d:	4c 8d 5c 17 f0       	lea    r11,[rdi+rdx*1-0x10]
   b8062:	48 8d 4c 16 f0       	lea    rcx,[rsi+rdx*1-0x10]
   b8067:	4d 89 d9             	mov    r9,r11
   b806a:	4d 89 d8             	mov    r8,r11
   b806d:	49 83 e0 0f          	and    r8,0xf
   b8071:	4c 29 c1             	sub    rcx,r8
   b8074:	4d 29 c1             	sub    r9,r8
   b8077:	4c 29 c2             	sub    rdx,r8
   b807a:	48 3b 15 17 ef 12 00 	cmp    rdx,QWORD PTR [rip+0x12ef17]        # 1e6f98 <_obstack@GLIBC_2.2.5+0x80>
   b8081:	0f 87 af 00 00 00    	ja     b8136 <memcpy@GLIBC_2.2.5+0x376>
   b8087:	0f 10 01             	movups xmm0,XMMWORD PTR [rcx]
   b808a:	0f 10 49 f0          	movups xmm1,XMMWORD PTR [rcx-0x10]
   b808e:	0f 10 51 e0          	movups xmm2,XMMWORD PTR [rcx-0x20]
   b8092:	0f 10 59 d0          	movups xmm3,XMMWORD PTR [rcx-0x30]
   b8096:	48 83 e9 40          	sub    rcx,0x40
   b809a:	48 83 ea 40          	sub    rdx,0x40
   b809e:	41 0f 29 01          	movaps XMMWORD PTR [r9],xmm0
   b80a2:	41 0f 29 49 f0       	movaps XMMWORD PTR [r9-0x10],xmm1
   b80a7:	41 0f 29 51 e0       	movaps XMMWORD PTR [r9-0x20],xmm2
   b80ac:	41 0f 29 59 d0       	movaps XMMWORD PTR [r9-0x30],xmm3
   b80b1:	49 83 e9 40          	sub    r9,0x40
   b80b5:	48 83 fa 40          	cmp    rdx,0x40
   b80b9:	77 cc                	ja     b8087 <memcpy@GLIBC_2.2.5+0x2c7>
   b80bb:	0f 11 27             	movups XMMWORD PTR [rdi],xmm4
   b80be:	0f 11 6f 10          	movups XMMWORD PTR [rdi+0x10],xmm5
   b80c2:	0f 11 77 20          	movups XMMWORD PTR [rdi+0x20],xmm6
   b80c6:	0f 11 7f 30          	movups XMMWORD PTR [rdi+0x30],xmm7
   b80ca:	45 0f 11 03          	movups XMMWORD PTR [r11],xmm8
   b80ce:	c3                   	ret    
   b80cf:	4c 8d 14 17          	lea    r10,[rdi+rdx*1]
   b80d3:	4c 39 d6             	cmp    rsi,r10
   b80d6:	0f 82 27 ff ff ff    	jb     b8003 <memcpy@GLIBC_2.2.5+0x243>
   b80dc:	0f 18 8e 80 00 00 00 	prefetcht0 BYTE PTR [rsi+0x80]
   b80e3:	0f 18 8e c0 00 00 00 	prefetcht0 BYTE PTR [rsi+0xc0]
   b80ea:	0f 10 06             	movups xmm0,XMMWORD PTR [rsi]
   b80ed:	0f 10 4e 10          	movups xmm1,XMMWORD PTR [rsi+0x10]
   b80f1:	0f 10 56 20          	movups xmm2,XMMWORD PTR [rsi+0x20]
   b80f5:	0f 10 5e 30          	movups xmm3,XMMWORD PTR [rsi+0x30]
   b80f9:	48 83 c6 40          	add    rsi,0x40
   b80fd:	48 83 ea 40          	sub    rdx,0x40
   b8101:	66 0f e7 07          	movntdq XMMWORD PTR [rdi],xmm0
   b8105:	66 0f e7 4f 10       	movntdq XMMWORD PTR [rdi+0x10],xmm1
   b810a:	66 0f e7 57 20       	movntdq XMMWORD PTR [rdi+0x20],xmm2
   b810f:	66 0f e7 5f 30       	movntdq XMMWORD PTR [rdi+0x30],xmm3
   b8114:	48 83 c7 40          	add    rdi,0x40
   b8118:	48 83 fa 40          	cmp    rdx,0x40
   b811c:	77 be                	ja     b80dc <memcpy@GLIBC_2.2.5+0x31c>
   b811e:	0f ae f8             	sfence 
   b8121:	0f 11 29             	movups XMMWORD PTR [rcx],xmm5
   b8124:	0f 11 71 f0          	movups XMMWORD PTR [rcx-0x10],xmm6
   b8128:	0f 11 79 e0          	movups XMMWORD PTR [rcx-0x20],xmm7
   b812c:	44 0f 11 41 d0       	movups XMMWORD PTR [rcx-0x30],xmm8
   b8131:	41 0f 11 23          	movups XMMWORD PTR [r11],xmm4
   b8135:	c3                   	ret    
   b8136:	4c 8d 14 11          	lea    r10,[rcx+rdx*1]
   b813a:	4d 39 d1             	cmp    r9,r10
   b813d:	0f 82 44 ff ff ff    	jb     b8087 <memcpy@GLIBC_2.2.5+0x2c7>
   b8143:	0f 18 49 80          	prefetcht0 BYTE PTR [rcx-0x80]
   b8147:	0f 18 89 40 ff ff ff 	prefetcht0 BYTE PTR [rcx-0xc0]
   b814e:	0f 10 01             	movups xmm0,XMMWORD PTR [rcx]
   b8151:	0f 10 49 f0          	movups xmm1,XMMWORD PTR [rcx-0x10]
   b8155:	0f 10 51 e0          	movups xmm2,XMMWORD PTR [rcx-0x20]
   b8159:	0f 10 59 d0          	movups xmm3,XMMWORD PTR [rcx-0x30]
   b815d:	48 83 e9 40          	sub    rcx,0x40
   b8161:	48 83 ea 40          	sub    rdx,0x40
   b8165:	66 41 0f e7 01       	movntdq XMMWORD PTR [r9],xmm0
   b816a:	66 41 0f e7 49 f0    	movntdq XMMWORD PTR [r9-0x10],xmm1
   b8170:	66 41 0f e7 51 e0    	movntdq XMMWORD PTR [r9-0x20],xmm2
   b8176:	66 41 0f e7 59 d0    	movntdq XMMWORD PTR [r9-0x30],xmm3
   b817c:	49 83 e9 40          	sub    r9,0x40
   b8180:	48 83 fa 40          	cmp    rdx,0x40
   b8184:	77 bd                	ja     b8143 <memcpy@GLIBC_2.2.5+0x383>
   b8186:	0f ae f8             	sfence 
   b8189:	0f 11 27             	movups XMMWORD PTR [rdi],xmm4
   b818c:	0f 11 6f 10          	movups XMMWORD PTR [rdi+0x10],xmm5
   b8190:	0f 11 77 20          	movups XMMWORD PTR [rdi+0x20],xmm6
   b8194:	0f 11 7f 30          	movups XMMWORD PTR [rdi+0x30],xmm7
   b8198:	45 0f 11 03          	movups XMMWORD PTR [r11],xmm8
   b819c:	c3                   	ret    
   b819d:	0f 1f 00             	nop    DWORD PTR [rax]
