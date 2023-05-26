INSERT INTO BUS_UNIT
SELECT SUBSTR(A.BUS_UNIT,0,3)||'|'||B.PIN||SUBSTR(B.GEO_NM,0,3) AS BUS_UNIT_CD FROM BUS_UNIT_STG A, LEFT JOIN GEO B ON A.GEO_PIN_CODE= B.GEO_PIN WHERE A.ELETE_DTM IS NOT NULL;