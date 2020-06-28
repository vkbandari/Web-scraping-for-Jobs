-- create mindaddadb1 database

use mindaddadb1;

show tables;
select * from analytics_jobs_tbl;

select * from raw_internshala_source_tbl;


CREATE TABLE IF NOT EXISTS `raw_internshala_scrape` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(50) DEFAULT NULL,
  `location` varchar(90) DEFAULT NULL,
  `job_link` varchar(256) DEFAULT NULL,
  `job_title` varchar(1020) DEFAULT NULL,
  `company_name` varchar(1020) DEFAULT NULL,
  `imp_fields` varchar(1020) DEFAULT NULL,
  `description_headings` varchar(256) DEFAULT NULL,
  `description` varchar(8040) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=136757 DEFAULT CHARSET=utf8;

select * from raw_internshala_scrape;



CREATE TABLE IF NOT EXISTS `raw_indeed_scrape` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(50) DEFAULT NULL,
  `job_title` varchar(90) DEFAULT NULL,
  `company_name` varchar(256) DEFAULT NULL,
  `salary` varchar(1020) DEFAULT NULL,
  `location` varchar(1020) DEFAULT NULL,
  `short_summary` varchar(1020) DEFAULT NULL,
  `link` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=136757 DEFAULT CHARSET=utf8;


select * from raw_indeed_scrape;



CREATE TABLE IF NOT EXISTS `raw_fb_scrape` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(50) DEFAULT 'facebook',
  `post_id` varchar(90) DEFAULT NULL,
  `text` varchar(1020) DEFAULT NULL,
  `post_text` varchar(1020) DEFAULT NULL,
  `shared_text` varchar(1020) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `likes` varchar(10) DEFAULT NULL, 
  `comments` varchar(10) DEFAULT NULL,
  `shares` varchar(10) DEFAULT NULL,
  `link` varchar(256) DEFAULT NULL,
  `jobs_info` varchar(50000) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


select * from raw_fb_scrape;



