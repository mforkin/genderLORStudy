I ran this script to convert all pdfs to sharp images for tessearct ocr to process

for f in *pages; do cd $f; ls | xargs -I{} -L1 sh -c "convert -density 150 -trim -quality 100 -flatten -sharpen 0x1.0 '{}' '{}.jpg'"; cd ..; done;

convert is from imagemagick
