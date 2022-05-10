--(2.1. ネコがフォローしているユーザー)
SELECT u2.name
FROM users as u1
INNER JOIN follows
ON u1.id = follows.follower_id
INNER JOIN users as u2
ON u2.id = followee_id
WHERE follower_id = 3


--(2.1. 誰もフォローしていないユーザ)
SELECT name
FROM users LEFT OUTER JOIN follows
  ON users.id = follows.follower_id  
WHERE follower_id IS NULL;



--(2.3. 相互フォローしているid一覧)
SELECT CONCAT(CAST(F1.follower_id AS CHAR), 'と', CAST(F2.follower_id AS CHAR)) AS '相互フォロー'
FROM follows AS F1 INNER JOIN follows AS F2
ON  F1.follower_id = F2.followee_id
AND F1.followee_id = F2.follower_id
WHERE F1.follower_id < F2.follower_id;


 

