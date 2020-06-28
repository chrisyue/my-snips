# my-snips

My snippets for Ultisnips, mainly for languages of web development, like
PHP, HTML, CSS, SASS, .etc.

Also I am a fan of Symfony, so there are many snips about Symfony, Doctrine
, Twig, .etc.

With the Python power integrated into Ultisnips, my-snips can auto generate
complex code snippets, like generating namespace according to the filepath
or `composer.json`'s `psr-4` information, or auto generating class, abstract
class, interface or trait according to the file name.

Please check the
[snippet files](https://github.com/chrisyue/my-snips/tree/master/UltiSnips)
to get more details

![namespace and class](http://img.chrisyue.com/nc-class.gif "namespace and class")

# installation

Assuming you are using [Vundle](https://github.com/gmarik/Vundle.vim), or
[vim-plugin](https://github.com/junegunn/vim-plug), Put the code below into
your `.vimrc`:

```
Plugin 'chrisyue/my-snippets'
"Or Plug 'chrisyue/my-snippets' if vim-plugin is used
```

then run `:PluginInstall`, or `:PlugInstall` if vim-plugin is used.
