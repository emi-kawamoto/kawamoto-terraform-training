SELECT
  CASE
    WHEN str2 = "太郎" THEN "花子"
  ELSE NULL
  END AS "太郎→花子"

FROM `SampleStr`
WHERE str2 = "太郎";
