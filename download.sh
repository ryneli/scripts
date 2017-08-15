IN_FILE=$1
OUT_FILE=$2
TMP_DIR=tmp
mkdir $TMP_DIR
index=0
for link in `grep -i cdn $IN_FILE`; do
    extension="${link##*.}"
    outpath=$TMP_DIR/`printf "%04d" $index`.$extension
    wget $link -O $outpath
    echo $outpath
    let index=${index}+1
done

cat `ls $TMP_DIR` > $OUT_FILE
