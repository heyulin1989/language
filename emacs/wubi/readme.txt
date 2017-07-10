;; 解压wubi.tar.gz 将解压出的文件复制到指定文件夹中
;; 使用add-to-list 'load-path 加载对应的文件
;; 这里将文件放在了~/.emacs.d/site-list/wubi目录下
;; 将下面的代码copy到~/.emacs中
(add-to-list 'load-path "~/.emacs.d/site-lisp/wubi")

(require 'wubi)
(wubi-load-local-phrases) ; add user's Wubi phrases

(register-input-method
 "chinese-wubi" "Chinese-GB" 'quail-use-package
 "WuBi" "WuBi"
 "wubi")

(if (< emacs-major-version 21)
    (setup-chinese-gb-environment)
  (set-language-environment 'Chinese-GB))

(setq default-input-method "chinese-wubi")
