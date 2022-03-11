# Little-Cases
Some scripts for convenience.



## Markdown Images Rearrangement

Move all the images appeared in the markdown to a relative/definite path directory.

```bash
Usage :
$ python arrange_md_img.py -i <inputfile> -o <outputfile> -m <imgdir>
-i <inputfile> [ifile= ] : the source markdown file
-o <outputfile> [ofile= ] : the new rearranged markdown file
-m <images dir> [imgdir= ]: the imgs will be copied to this directory, the default is "./img"
```



## Remote Class for Sage

Since pwn repo can't be installed successfully in sage on Windows OS ,I implement a simple class : `remote` for nc interaction in CTF challenges.

  
