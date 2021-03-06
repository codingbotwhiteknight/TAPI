#! bash
MODULES=(
[0]='tapi-common'
[1]='tapi-common tapi-notification'
[2]='tapi-common tapi-notification tapi-topology'
[3]='tapi-common tapi-notification tapi-topology tapi-equipment'
[4]='tapi-common tapi-notification tapi-topology tapi-virtual-network'
[5]='tapi-common tapi-notification tapi-topology tapi-path-computation'
[6]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity'
[7]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity tapi-oam'
[8]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity tapi-oam tapi-dsr'
[9]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity tapi-oam tapi-dsr tapi-odu'
[10]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity tapi-oam tapi-dsr tapi-eth'
[11]='tapi-common tapi-notification tapi-topology tapi-path-computation tapi-connectivity tapi-oam tapi-dsr tapi-odu tapi-photonic-media'
)

echo "Generating OpenAPI files from YANG files"
for elt in "${!MODULES[@]}"; do
  for module in ${MODULES[$elt]}; do
    yangfile=$(find ./YANG/ -name "${module}*.yang")
    tmpfile=`echo ${yangfile##*/} | sed 's/yang//g'`;
    oasfile=./OAS/${tmpfile}yaml
    cp ${yangfile} ./TMP/${tmpfile}yang
  done
  echo "Generating ${oasfile}"
  java -jar swagger-generator-cli-1.1.13-executable.jar -api-version 2.2.0 -yang-dir ./TMP/ -output ${oasfile} &> "./TMP/${tmpfile}log"
  sed -i '/originalRef/d' ${oasfile}
  sed -i '/responseSchema/{N;d;}' ${oasfile}
  rm ./TMP/*.yang
done
