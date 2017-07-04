EMMS is the Emacs Multi-Media System. It tries to be a clean and small application to play multimedia files from
Emacs using external players. Many of the ideas are derived from MpthreePlayer, but it tries to be more general
and cleaner. It is comparable to Bongo
http://www.gnu.org/software/emms/
http://www.gnu.org/software/emms/quickstart.html

git clone git://git.sv.gnu.org/emms.git
or
git clone git://git.sv.gnu.org/r/emms.git

use it:
(add-to-list 'load-path '~/elisp/emms/')
(require 'emms-setup)
(emms-standard)
(emms-default-players)

