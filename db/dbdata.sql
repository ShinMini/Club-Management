DROP TABLE IF EXISTS member;
CREATE TABLE member(
       member_id    INT AUTO_INCREMENT PRIMARY KEY,
       member_name  VARCHAR(255) NOT NULL,
       age          int NOT NULL,
       phone        VARCHAR(255) NOT NULL,
       gender       char(25),
       club_name    VARCHAR(255) NOT NULL,
       rating       VARCHAR(255) NOT NULL,
       enroll       VARCHAR(255)
);  
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('박재상', 40, '010-1111-2222', 'M', '서울특별시배드민턴협회', 'D', '2000-02-02');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('현민', 24, '010-8794-3202', 'M', '경기도배드민턴협회', 'D', '2022-09-14');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('종국', 42, "010-1234-5678", 'M', '서울특별시배드민턴협회', 'A', '1999-05-01');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('신선', 20, "010-1455-7845", 'F', '대구광역시배드민턴협회', 'B', '2010-05-01');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('정시준', 30, "010-1645-7514", 'M', '충청북도배드민턴협회', 'A', '2010-04-01');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('성익제', 40, "010-1643-9865", 'M', '제주특별자치도배드민턴협회', 'C', '2002-04-01');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('유재석', 50, "010-3215-6596", 'M', '전라남도배드민턴협회', 'D', '2012-04-01');
INSERT INTO member (member_name, age, phone, gender, club_name, rating, enroll)
VALUES ('노홍철', 42, "010-1574-9635", 'M', '경상북도배드민턴협회', 'S', '2012-04-01');