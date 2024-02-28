CREATE SEQUENCE skill_id_seq;
CREATE SEQUENCE scout_id_seq;
CREATE SEQUENCE job_code_seq;
CREATE SEQUENCE ad_id_seq;
CREATE SEQUENCE article_id_seq;
CREATE SEQUENCE question_id_seq;
CREATE SEQUENCE defect_report_id_seq;
CREATE SEQUENCE report_id_seq;
CREATE SEQUENCE work_id_seq;
CREATE SEQUENCE post_id_seq;
CREATE SEQUENCE message_id_seq;
CREATE SEQUENCE career_id_seq;
CREATE SEQUENCE operator_id_seq;

CREATE TABLE skill_t (
    skill_id INTEGER PRIMARY KEY DEFAULT nextval('skill_id_seq'),
    skill_name VARCHAR(48) UNIQUE NOT NULL,
    skill_icon VARCHAR(255) NOT NULL
);
CREATE TABLE message_status_t (
    message_status_code INTEGER PRIMARY KEY,
    message_status VARCHAR(15) UNIQUE NOT NULL
);
CREATE TABLE message_type_t (
    message_type_code INTEGER PRIMARY KEY,
    message_type VARCHAR(15) UNIQUE NOT NULL
);
CREATE TABLE relation_t (
    relation_code INTEGER PRIMARY KEY,
    relation_status VARCHAR(30) NOT NULL
);
CREATE TABLE company_info_t (
    company_id VARCHAR(36) PRIMARY KEY ,
    subscription_status BOOLEAN NOT NULL,
    company_mail_address VARCHAR(255) UNIQUE NOT NULL,
    company_pass VARCHAR(32) NOT NULL,
    tel_num VARCHAR(16) UNIQUE NOT NULL,
    company_address VARCHAR(255) NOT NULL,
    company_web VARCHAR(255) ,
    company_name VARCHAR(450) NOT NULL,
    company_header_image VARCHAR(255) ,
    company_logomark VARCHAR(255) NOT NULL ,
    company_explanation VARCHAR(1500),
    postalcode VARCHAR(8) NOT NULL,
    company_notice_status VARCHAR(4) NOT NULL
);
-- company_web,company_logomark,company_header_imageをサンプルデータのため、UNIQUE制約を一旦取り消し
CREATE TABLE scout_t (
    scout_id INTEGER PRIMARY KEY DEFAULT nextval('scout_id_seq'),
    company_id VARCHAR(36) REFERENCES company_info_t(company_id),
    scout_start_at DATE NOT NULL,
    scout_end_at DATE NOT NULL,
    scout_body VARCHAR(3000) NOT NULL
);
CREATE TABLE employment_code_t (
    employment_code INTEGER PRIMARY KEY,
    employment_status VARCHAR(30) NOT NULL UNIQUE
);
CREATE TABLE job_code_t (
    job_code INTEGER PRIMARY KEY,
    job_name VARCHAR(75) NOT NULL UNIQUE
);
CREATE TABLE reward_t (
    reward_code INTEGER PRIMARY KEY,
    reward_status VARCHAR(6) UNIQUE NOT NULL
);
CREATE TABLE advertisement_t (
    ad_id INTEGER PRIMARY KEY DEFAULT nextval('ad_id_seq'),
    company_id VARCHAR(36) REFERENCES company_info_t(company_id),
    ad_start_at DATE NOT NULL,
    ad_end_at DATE NOT NULL,
    impression INTEGER NOT NULL ,
    ad_image VARCHAR(255) NOT NULL ,
    ad_web VARCHAR(255) ,
    ad_body VARCHAR(420),
    ad_expenses INTEGER NOT NULL ,
    click_num INTEGER NOT NULL ,
    notice_operation VARCHAR(255)
);
CREATE TABLE advertisement_sex_code_t (
    ad_id INTEGER PRIMARY KEY REFERENCES advertisement_t(ad_id),
    sex_code VARCHAR(3) NOT NULL
);
CREATE TABLE article_t (
    article_id INTEGER PRIMARY KEY DEFAULT nextval('article_id_seq'),
    company_id VARCHAR(36) REFERENCES company_info_t(company_id),
    article_title VARCHAR(90) NOT NULL ,
    article_thumbnail VARCHAR(255) NOT NULL ,
    article_body VARCHAR (3000) NOT NULL ,
    article_at TIMESTAMP NOT NULL ,
    article_impression INTEGER NOT NULL ,
    article_image1 VARCHAR(255),
    article_image2 VARCHAR(255),
    article_image3 VARCHAR(255),
    tag_1 VARCHAR(60),
    tag_2 VARCHAR(60),
    tag_3 VARCHAR(60),
    tag_4 VARCHAR(60),
    tag_5 VARCHAR(60),
    article_summary VARCHAR(511),
    hidden_flag BOOLEAN NOT NULL
);
CREATE TABLE question_t (
    question_id INTEGER PRIMARY KEY DEFAULT nextval('question_id_seq'),
    company_id VARCHAR(36) REFERENCES company_info_t(company_id),
    question_title VARCHAR(90),
    question VARCHAR(255),
    answer VARCHAR(511)
);
CREATE TABLE template_t (
    company_id VARCHAR(36) PRIMARY KEY REFERENCES company_info_t(company_id),
    template_1 VARCHAR(3000),
    template_2 VARCHAR(3000),
    template_3 VARCHAR(3000),
    template_4 VARCHAR(3000),
    template_5 VARCHAR(3000),
    template_6 VARCHAR(3000),
    template_7 VARCHAR(3000),
    template_8 VARCHAR(3000),
    template_9 VARCHAR(3000),
    template_10 VARCHAR(3000)
);
CREATE TABLE report_code_t (
    report_code INTEGER PRIMARY KEY,
    report VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE del_reason_code_t (
    del_reason_code INTEGER PRIMARY KEY,
    del_reason VARCHAR(255) NOT NULL
);
CREATE TABLE company_delete_request_t (
    company_id VARCHAR(36) PRIMARY KEY,
    del_reason_code INTEGER REFERENCES del_reason_code_t(del_reason_code)
);
CREATE TABLE operator_t (
    operator_id VARCHAR(8) PRIMARY KEY DEFAULT('O' || LPAD(nextval('operator_id_seq')::text, 7, '0')),
    operator_pass VARCHAR(32) NOT NULL,
    active_operator_flag BOOLEAN NOT NULL
);
CREATE TABLE advertisement_approval_t (
    ad_id INTEGER PRIMARY KEY REFERENCES advertisement_t(ad_id),
    ad_approval_flag BOOLEAN,
    operator_id VARCHAR(8) REFERENCES operator_t(operator_id)
);
CREATE TABLE company_approval_t (
    company_id VARCHAR(8) PRIMARY KEY REFERENCES company_info_t(company_id),
    tel_num VARCHAR(11),
    company_name VARCHAR(90),
    company_approval_flag BOOLEAN
);
CREATE TABLE work_t (
    work_id INTEGER PRIMARY KEY DEFAULT nextval('work_id_seq'),
    company_id VARCHAR(36) REFERENCES company_info_t(company_id),
    employment_code INTEGER REFERENCES employment_code_t(employment_code),
    job_code INTEGER REFERENCES job_code_t(job_code) NOT NULL ,
    work_title VARCHAR(90) NOT NULL ,
    work_content VARCHAR(1500) NOT NULL ,
    require_skills VARCHAR(600) NOT NULL ,
    suit_person VARCHAR(1500) NOT NULL ,
    area_code VARCHAR(100) NOT NULL,
    rating INTEGER NOT NULL ,
    avg_portfolio REAL NOT NULL ,
    contract_start_at TIMESTAMP NOT NULL ,
    contract_end_at TIMESTAMP NOT NULL ,
    reward_code INTEGER REFERENCES reward_t(reward_code),
    reward INTEGER NOT NULL ,
    reward_tax_flag INTEGER NOT NULL ,
    transport_cost INTEGER NOT NULL ,
    work_image VARCHAR(255) NOT NULL ,
    sex_code VARCHAR(3) NOT NULL,
    work_time VARCHAR(150) NOT NULL ,
    require_skills_flag BOOLEAN NOT NULL ,
    suit_person_flag BOOLEAN NOT NULL ,
    rating_flag BOOLEAN NOT NULL ,
    avg_portfolio_flag BOOLEAN NOT NULL ,
    contract_start_at_flag BOOLEAN NOT NULL ,
    contract_end_at_flag BOOLEAN NOT NULL ,
    reward_flag BOOLEAN NOT NULL ,
    work_time_flag BOOLEAN NOT NULL ,
    transport_cost_flag BOOLEAN NOT NULL ,
    sex_flag BOOLEAN NOT NULL
);
CREATE TABLE work_area_t (
    work_id INTEGER PRIMARY KEY REFERENCES work_t(work_id),
    area_code VARCHAR(100) NOT NULL
);
CREATE TABLE student_info_t (
    student_id VARCHAR(36) PRIMARY KEY,
    mail_address VARCHAR(255) UNIQUE NOT NULL,
    student_pass VARCHAR(32) NOT NULL,
    handle_name VARCHAR(30) NOT NULL,
    family_name VARCHAR(30) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    sex_code varchar(3) NOT NULL,
    area_code VARCHAR(100) NOT NULL,
    faculty VARCHAR(75) NOT NULL,
    department VARCHAR(75) NOT NULL,
    birthday DATE NOT NULL,
    expected_graduation DATE NOT NULL,
    header_image VARCHAR(255) NOT NULL,
    profile_image VARCHAR(255),
    motto VARCHAR(255),
    student_intro VARCHAR(90),
    web_link VARCHAR(255),
    post_num VARCHAR(255),
    rating_point INTEGER,
    avg_portfolio REAL,
    student_card_flag BOOLEAN NOT NULL,
    notice_status VARCHAR(4) NOT NULL,
    student_interest VARCHAR(30)
);
CREATE TABLE student_approval_t (
    student_id VARCHAR(36) PRIMARY KEY,
    student_image VARCHAR(255) NOT NULL
);
-- student_imageをサンプルデータのため、UNIQUE制約を一旦取り消し
CREATE TABLE advertisement_area_t (
    ad_id VARCHAR(8) PRIMARY KEY,
    area_code VARCHAR(100) NOT NULL
);
CREATE TABLE work_achivement_t (
    student_id VARCHAR(36) REFERENCES student_info_t(student_id),
    work_id INTEGER REFERENCES work_t(work_id),
    achievement_flag BOOLEAN NOT NULL ,
    score REAL NOT NULL ,
    manager_comment VARCHAR(255),
    PRIMARY KEY(student_id, work_id)
);
CREATE TABLE user_relation_t (
    user_id_from VARCHAR(36) REFERENCES student_info_t(student_id),
    user_id_to VARCHAR(36) REFERENCES student_info_t(student_id),
    relation_code INTEGER REFERENCES relation_t(relation_code),
    PRIMARY KEY(user_id_from, user_id_to)
);
CREATE TABLE student_scout_t (
    scout_user_id VARCHAR(36) REFERENCES student_info_t(student_id),
    scout_id INTEGER REFERENCES scout_t(scout_id),
    isAccepted BOOLEAN NOT NULL ,
    PRIMARY KEY(scout_user_id, scout_id)
);
CREATE TABLE timeline_t (
    post_id INTEGER PRIMARY KEY DEFAULT nextval('post_id_seq'),
    user_id VARCHAR(36) NOT NULL,
    impression_num INTEGER NOT NULL,
    timeline_created_at TIMESTAMP NOT NULL,
    reply_post_id INTEGER,
    reply_to VARCHAR(36),
    post_body VARCHAR(300) NOT NULL,
    hidden_status INTEGER NOT NULL
);
CREATE TABLE bookmarked_post_t(
    post_id INTEGER REFERENCES timeline_t(post_id),
    user_id VARCHAR(36),
    PRIMARY KEY(post_id, user_id)
);
CREATE TABLE liked_post_t (
    post_id INTEGER REFERENCES timeline_t(post_id),
    user_id VARCHAR(36),
    PRIMARY KEY(post_id, user_id)
);
CREATE TABLE message_t (
    message_id INTEGER PRIMARY KEY DEFAULT nextval('message_id_seq'),
    message_from VARCHAR(36) NOT NULL,
    message_to VARCHAR(36) NOT NULL,
    message_type_code INTEGER REFERENCES message_type_t(message_type_code) NOT NULL,
    message_body VARCHAR(3000) NOT NULL,
    message_status_code INTEGER REFERENCES message_status_t(message_status_code) NOT NULL,
    work_or_scout_id INTEGER,
    message_created_at TIMESTAMP NOT NULL
);
CREATE TABLE career_info_t (
    career_id INTEGER DEFAULT nextval('career_id_seq'),
    student_id VARCHAR(36) REFERENCES student_info_t(student_id),
    affiliation_id INTEGER NOT NULL,
    career_title VARCHAR(48) NOT NULL,
    career_detail VARCHAR(600) NOT NULL,
    career_start_at DATE NOT NULL,
    career_end_at DATE NOT NULL,
    publication_status INTEGER NOT NULL,
    carrer_type_code INTEGER NOT NULL,
    result_num INTEGER,
    carrer_image_1 VARCHAR(255),
    carrer_image_2 VARCHAR(255),
    carrer_image_3 VARCHAR(255),
    PRIMARY KEY(student_id, career_id)
);
CREATE TABLE student_skill_t (
    student_id VARCHAR(36) REFERENCES student_info_t(student_id),
    skill_id INTEGER REFERENCES skill_t(skill_id),
    skill_text VARCHAR(450) NOT NULL,
    PRIMARY KEY(student_id, skill_id)
);
CREATE TABLE report_users_t (
    report_id varchar(8) PRIMARY KEY DEFAULT nextval('report_id_seq'),
    student_id varchar(36) REFERENCES student_info_t(student_id),
    post_id INTEGER REFERENCES timeline_t(post_id),
    report_code INTEGER REFERENCES report_code_t(report_code),
    report_approval_flag BOOLEAN,
    operator_id varchar(8) REFERENCES operator_t(operator_id)
);