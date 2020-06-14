I ran this script to convert all pdfs to sharp images for tessearct ocr to process

This is for jpg, quality is determining the level of compression
`sh for f in *pages; do cd $f; ls | xargs -I{} -L1 sh -c "convert -density 150 -trim -quality 100 -flatten -sharpen 0x1.0 '{}' '{}.jpg'"; cd ..; done;`

This is for png, no quality b\c it is lossless, also upped the density for better text extraction
`sh for f in *pages; do cd $f; ls | xargs -I{} -L1 sh -c "convert -density 600 -trim -sharpen 0x1.0 '{}' '{}.jpg'"; cd ..; done;`
convert is from imagemagick

## Update for thresholding

ls 582C.pdf | xargs -I{} -P7 sh -c "convert -density 600 -trim -quality 100 -flatten -sharpen 0x1.0 -black-threshold 50% -white-threshold 50% '{}' '{}.jpg'"

