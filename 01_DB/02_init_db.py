import json
import pymysql

with open('mysql.json', 'r') as file:
    config_str = file.read()
config = json.loads(config_str)

conn = pymysql.connect(
    host = config['host'],
    user = config['user'],
    password = config['password'],
    database = config['database'],
    port = config['port']
)

sqlUsers = """
    create table if not exists users (
        uid varchar(20) not null primary key,
        pwd char(44) not null,
        uname varchar(20) not null,
        tel varchar(20),
        email varchar(40),
        regDate datetime default current_timestamp,
        isDeleted int default 0,
        photo varchar(80)
    );
"""
sqlBbs = """
    create table if not exists bbs (
        bid int not null primary key auto_increment,
        uid varchar(20) not null,
        title varchar(100) not null,
        content varchar(1000),
        modTime datetime default current_timestamp,
        viewCount int default 0,
        isDeleted int default 0,
        replyCount int default 0,
        foreign key(uid) references users(uid)
    ) auto_increment=1001;
"""
sqlReplyBbs = """
    create table if not exists reply (
        rid int not null primary key auto_increment,
        bid int not null,
        uid varchar(20) not null,
        content varchar(100),
        regTime datetime default current_timestamp,
        isMine int default 0,
        foreign key(bid) references bbs(bid),
        foreign key(uid) references users(uid)
    );
"""
users = [
    ('admin', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', '관리자', '010-1111-1111', 'admin@naver.com', '/upload/blank.png'),
    ('park', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', '박주영', '010-1234-5678', 'park@naver.com', '/upload/blank.png'),
    ('lee', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', '이근', '010-1212-1212', 'KenRhee@naver.com', '/upload/blank.png'),
    ('choi', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', '최강현', '010-1235-5679', 'hoseo@hoseo.com', '/upload/blank.png'),
    ('aaa', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', 'guest1', '010-2654-1253', 'hoseo1@hoseo.com', '/upload/blank.png'),
    ('bbb', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', 'guest2', '02-2222-2222', 'hoseo2@hoseo.com', '/upload/blank.png'),
    ('ccc', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', 'guest3', '02-3333-3333', 'hoseo3@hoseo.com', '/upload/blank.png'),
    ('ddd', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', 'guest4', '02-4444-4444', 'hoseo4@hoseo.com', '/upload/blank.png'),
    ('eee', 'A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=', 'guest5', '02-5555-5555', 'hoseo5@hoseo.com', '/upload/blank.png')
]
sqlRegister = 'insert into users(uid, pwd, uname, tel, email, photo) values(%s,%s,%s,%s,%s,%s);'
bbsList = [
    ('admin', '미스터 션샤인', '2018년 방영한, 구한말을 배경으로 하는 한국 드라마.'),
    ('admin', '도깨비', '불멸의 삶을 끝내기 위해 인간 신부가 필요한 도깨비(공유)와 그와 함께 기묘한 동거를 시작한 기억상실증 저승사자(이동욱). 그런 그들 앞에 \'도깨비 신부\'라 주장하는 \'죽었어야 할 운명\'의 소녀 지은탁(김고은)이 나타나며 벌어지는 신비로운 낭만설화이다.'),
    ('park', '태양의 후예', '선 땅 극한의 환경 속에서 사랑과 성공을 꿈꾸는 젊은 군인과 의사들을 통해 삶의 가치를 담아낸 블록버스터급 휴먼 멜로 드라마'),
    ('park', '시크릿 가든', '가지 없는 부잣집 도련님과 스턴트맨으로 하루하루 간신히 살아가는 도시 빈민 아가씨의 연애라는 진부하기 짝이 없는 설정, 거기에 남녀의 영혼이 뒤바뀐다는 클리셰를 사용하였다.'),
    ('lee', '파리의 연인', '''"애기야 가자"
    "저 남자가 내 사람이다. 저 남자가 내 애인이다 왜 말을 못하냐고!"'''),
    ('lee', '슬기로운 의사생활', '누군가는 태어나고 누군가는 삶을 끝내는, 인생의 축소판이라 불리는 병원에서 평범한 듯 특별한 하루하루를 살아가는 사람들과 눈빛만 봐도 알 수 있는 20년지기 친구들의 케미스토리를 담은 드라마. 99학번 의대 동기 다섯 명을 중심으로 펼쳐지는 병원에서의 이야기를 그린다.')
]
sqlInsert = 'insert into bbs(uid, title, content) values(%s, %s, %s);'
replyList = [
    (1005, 'aaa', '좋습니다. 매우 훌륭한 작품입니다.'),
    (1005, 'bbb', '매우매우 훌륭합니다.'),
    (1006, 'ddd', '너무 좋은 작품입니다. 잘 보았어요.')
]
sqlInsertReply = 'insert into reply(bid, uid, content) values(%s, %s, %s);'
bbsReplyList = [
    (1, 1, 1006), (2, 2, 1005)
]
sqlReplyUpdate = 'update bbs set viewCount=%s, replyCount=%s where bid=%s;'

cur = conn.cursor()
cur.execute(sqlUsers)
conn.commit()
cur.executemany(sqlRegister, users)
conn.commit()

cur = conn.cursor()
cur.execute(sqlBbs)
conn.commit()
cur.executemany(sqlInsert, bbsList)
conn.commit()

cur = conn.cursor()
cur.execute(sqlReplyBbs)
conn.commit()
cur.executemany(sqlInsertReply, replyList)
conn.commit()
cur.executemany(sqlReplyUpdate, bbsReplyList)
conn.commit()

cur.close()
conn.close()