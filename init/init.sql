CREATE SEQUENCE skill_id_seq;
CREATE SEQUENCE message_status_code_seq;
CREATE SEQUENCE message_type_code_seq;
CREATE SEQUENCE relation_code_seq;
CREATE SEQUENCE scout_id_seq;
CREATE SEQUENCE employment_code_seq;
CREATE SEQUENCE job_code_seq;
CREATE SEQUENCE reward_code_seq;
CREATE SEQUENCE ad_id_seq;
CREATE SEQUENCE sex_code_seq;
CREATE SEQUENCE article_id_seq;
CREATE SEQUENCE question_id_seq;
CREATE SEQUENCE report_code_seq;
CREATE SEQUENCE del_reason_code_seq;
CREATE SEQUENCE defect_report_id_seq;
CREATE SEQUENCE work_id_seq;
CREATE SEQUENCE post_id_seq;
CREATE SEQUENCE message_id_seq;
CREATE SEQUENCE career_id_seq;
CREATE SEQUENCE company_id_seq START 0000001;
CREATE SEQUENCE student_id_seq START 0000001;
CREATE SEQUENCE operator_id_seq START 0000001;


CREATE TABLE skill_t (
    skill_id INTEGER PRIMARY KEY ,
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
    company_id VARCHAR(8) PRIMARY KEY DEFAULT('c' || nextval('company_id_seq')),
    subscription_status INTEGER NOT NULL,
    company_mail_address VARCHAR(255) UNIQUE NOT NULL,
    company_pass VARCHAR(32) NOT NULL,
    tel_num VARCHAR(16) UNIQUE NOT NULL,
    company_address VARCHAR(255) NOT NULL,
    company_web VARCHAR(255) UNIQUE ,
    company_name VARCHAR(450) NOT NULL,
    company_header_image VARCHAR(255) UNIQUE ,
    company_logomark VARCHAR(255) UNIQUE NOT NULL ,
    company_explanation VARCHAR(1500),
    postalcode VARCHAR(8) NOT NULL,
    company_notice_status INTEGER NOT NULL
);

CREATE TABLE scout_t (
    scout_id INTEGER PRIMARY KEY,
    company_id VARCHAR(8) REFERENCES company_info_t(company_id),
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
    ad_id INTEGER PRIMARY KEY,
    company_id VARCHAR(8) REFERENCES company_info_t(company_id),
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

CREATE TABLE sex_t (
    sex_code INTEGER PRIMARY KEY,
    sex_name VARCHAR(9) UNIQUE NOT NULL
);

CREATE TABLE advertisement_sex_code_t (
    ad_id INTEGER PRIMARY KEY REFERENCES advertisement_t(ad_id),
    sex_code INTEGER REFERENCES sex_t(sex_code)
);

CREATE TABLE article_t (
    article_id INTEGER PRIMARY KEY,
    company_id VARCHAR(8) REFERENCES company_info_t(company_id),
    article_title VARCHAR(90) NOT NULL ,
    article_thumbnail VARCHAR(255) NOT NULL ,
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
    question_id INTEGER PRIMARY KEY,
    company_id VARCHAR(8) REFERENCES company_info_t(company_id),
    question_title VARCHAR(90),
    question VARCHAR(255),
    answer VARCHAR(511)
);

CREATE TABLE template_t (
    company_id VARCHAR(8) PRIMARY KEY REFERENCES company_info_t(company_id),
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
    company_id VARCHAR(8) PRIMARY KEY,
    del_reason_code INTEGER REFERENCES del_reason_code_t(del_reason_code)
);

CREATE TABLE operator_t (
    operator_id VARCHAR(8) PRIMARY KEY DEFAULT('o' || nextval('operator_id_seq')),
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

CREATE TABLE defect_report_t (
    defect_report_id INTEGER PRIMARY KEY,
    skill_id VARCHAR(255) NOT NULL ,
    defect_reported_at DATE NOT NULL 
);

CREATE TABLE work_t (
    work_id INTEGER PRIMARY KEY,
    company_id VARCHAR(8) REFERENCES company_info_t(company_id),
    employment_code INTEGER REFERENCES employment_code_t(employment_code),
    job_code INTEGER REFERENCES job_code_t(job_code) NOT NULL ,
    work_title VARCHAR(90) NOT NULL ,
    work_content VARCHAR(1500) NOT NULL ,
    require_skills VARCHAR(600) NOT NULL ,
    suit_person VARCHAR(1500) NOT NULL ,
    area_code VARCHAR(10) NOT NULL,
    rating INTEGER NOT NULL ,
    avg_portfolio REAL NOT NULL ,
    contract_start_at TIMESTAMP NOT NULL ,
    contract_end_at TIMESTAMP NOT NULL ,
    reward_code INTEGER REFERENCES reward_t(reward_code),
    reward INTEGER NOT NULL ,
    reward_tax_flag INTEGER NOT NULL ,
    transport_cost INTEGER NOT NULL ,
    work_image VARCHAR(255) NOT NULL ,
    sex_code INTEGER REFERENCES sex_t(sex_code),
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
    area_code VARCHAR(10) NOT NULL
);


CREATE TABLE student_info_t (
    student_id VARCHAR(8) PRIMARY KEY DEFAULT('s' || nextval('student_id_seq')),
    mail_address VARCHAR(255) UNIQUE NOT NULL,
    student_pass VARCHAR(32) NOT NULL,
    handle_name VARCHAR(30) NOT NULL,
    family_name VARCHAR(30) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    sex_code INTEGER REFERENCES sex_t(sex_code),
    area_code VARCHAR(10) NOT NULL,
    faculty VARCHAR(75) NOT NULL,
    department VARCHAR(75) NOT NULL,
    birthday VARCHAR(75) NOT NULL,
    expected_graduation DATE NOT NULL,
    header_image DATE NOT NULL,
    profile_image VARCHAR(255),
    motto VARCHAR(255),
    student_intro VARCHAR(90),
    web_link VARCHAR(255),
    post_num VARCHAR(255),
    mail_address_count INTEGER,
    rating_point INTEGER,
    avg_portfolio REAL,
    student_card_flag BOOLEAN NOT NULL,
    notice_status INTEGER NOT NULL
);

CREATE TABLE student_approval_t (
    student_id VARCHAR(8) PRIMARY KEY,
    student_image VARCHAR(255) UNIQUE NOT NULL,
    operator_id VARCHAR(8) REFERENCES operator_t(operator_id) NOT NULL
);

CREATE TABLE advertisement_area_t (
    ad_id VARCHAR(8) PRIMARY KEY,
    area_code VARCHAR(10) NOT NULL
);

CREATE TABLE work_achivement_t (
    student_id VARCHAR(8) PRIMARY KEY REFERENCES student_info_t(student_id),
    work_id INTEGER REFERENCES work_t(work_id),
    achievement_flag BOOLEAN NOT NULL ,
    score REAL NOT NULL ,
    manager_comment VARCHAR(255)
);

CREATE TABLE user_relation_t (
    user_id_from VARCHAR(8) ,
    user_id_to VARCHAR(8) ,
    relation_code INTEGER REFERENCES relation_t(relation_code),
    PRIMARY KEY(user_id_from, user_id_to)
);

CREATE TABLE student_scout_t (
    scout_user_id VARCHAR(8) REFERENCES student_info_t(student_id),
    scout_id INTEGER REFERENCES scout_t(scout_id),
    isAccepted BOOLEAN NOT NULL ,
    PRIMARY KEY(scout_user_id, scout_id)
);

CREATE TABLE timeline_t (
    post_id INTEGER PRIMARY KEY,
    user_id VARCHAR(8) NOT NULL,
    impression_num INTEGER NOT NULL,
    timeline_created_at TIMESTAMP NOT NULL,
    reply_to VARCHAR(8),
    post_body VARCHAR(300) NOT NULL,
    hidden_status INTEGER NOT NULL
);

CREATE TABLE bookmarked_post_t(
    post_id INTEGER PRIMARY KEY REFERENCES timeline_t(post_id),
    user_id VARCHAR(8) NOT NULL 
);

CREATE TABLE liked_post_t (
    post_id INTEGER PRIMARY KEY REFERENCES timeline_t(post_id),
    user_id VARCHAR(8) NOT NULL
);

CREATE TABLE message_t (
    message_id INTEGER PRIMARY KEY,
    message_from VARCHAR(8) NOT NULL,
    message_to VARCHAR(8) NOT NULL,
    message_type_code INTEGER REFERENCES message_type_t(message_type_code) NOT NULL,
    message_body VARCHAR(3000) NOT NULL,
    message_status_code INTEGER REFERENCES message_status_t(message_status_code) NOT NULL,
    message_created_at TIMESTAMP NOT NULL
);

CREATE TABLE career_info_t (
    student_id VARCHAR(8),
    career_id INTEGER,
    career_title VARCHAR(48) NOT NULL,
    career_detail VARCHAR(600) NOT NULL,
    career_start_at DATE NOT NULL,
    career_end_at DATE NOT NULL,
    PRIMARY KEY (student_id, career_id),
    FOREIGN KEY (student_id) REFERENCES student_info_t(student_id)
);

CREATE TABLE student_skill_t (
    student_id VARCHAR(8) REFERENCES student_info_t(student_id),
    skill_id INTEGER REFERENCES skill_t(skill_id),
    skill_text VARCHAR(450) NOT NULL,
    PRIMARY KEY(student_id, skill_id)
);
