use redsnakes;
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS ORGANIZATION;
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS RESEARCH_TOPIC;
DROP TABLE IF EXISTS CONFERENCE;
DROP TABLE IF EXISTS CONFERENCE_CATEGORY;
DROP TABLE IF EXISTS PAPER;
DROP TABLE IF EXISTS REVIEW;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE ORGANIZATION(OrganizationID int(10) unsigned NOT NULL AUTO_INCREMENT,
Title varchar(255) not null,
primary key (OrganizationID)
);

CREATE TABLE USER(UserID int(10) unsigned NOT NULL AUTO_INCREMENT,
userCategory varchar(255) not null,
affiliation varchar(255) not null,
OrganizationID int(10) unsigned not null,
email varchar(255) not null,
fullName varchar(255) not null,
locationX float not null,
locationY float not null,
photoURL varchar(255) not null,
street varchar(255) not null,
FOREIGN KEY(OrganizationID) REFERENCES ORGANIZATION(OrganizationID),
primary key (UserID));


CREATE TABLE CONFERENCE(ConferenceID int(10) unsigned not null AUTO_INCREMENT,
Category varchar(255) not null,
coordsX float not null,
coordsY float not null,
deadlineAbstract date not null,
deadlineBiding date not null,
deadlinePaper date not null,
deadlineReview date not null,
description varchar(255) not null,
email varchar(255) not null,
startDate date not null,
endDate date not null,
ownerEmail date not null,
price int not null,
reasearchTopics varchar(255) not null,
title varchar(255) not null,
website varchar(255) not null,
primary key (ConferenceID));



CREATE TABLE CONFERENCE_CATEGORY(ConferenceCategoryID int(10) unsigned not null AUTO_INCREMENT,
Title varchar(255) not null,
ConferenceID int(10) unsigned not null,
FOREIGN KEY (ConferenceID) REFERENCES CONFERENCE(ConferenceID),
primary key (ConferenceCategoryID));

CREATE TABLE RESEARCH_TOPIC(ResearchTopicID int(10) unsigned not null AUTO_INCREMENT,
Category varchar(255) not null,
ConferenceCategoryID int(10) unsigned not null,
FOREIGN KEY (ConferenceCategoryID) REFERENCES CONFERENCE_CATEGORY(ConferenceCategoryID),
Name varchar(255) not null,
primary key (ResearchTopicID));


CREATE TABLE PAPER(PaperID int(10) unsigned not null AUTO_INCREMENT,
authorEmail varchar(255) not null,
conferenceID int(10) unsigned not null,
conferenceName varchar(255) not null,
fileURL varchar(255) not null,
status varchar(255) not null,
timestamp varchar(255) not null,
abstract varchar(10000),
title varchar(255) not null,
FOREIGN KEY (conferenceID) REFERENCES CONFERENCE(conferenceID),
primary key (PaperID));



CREATE TABLE REVIEW(UserID int(10) unsigned not null,
PaperID int(10) unsigned not null,
assignedReviewerEmail varchar(255) not null,
conferenceName varchar(255) not null,
paperTitle varchar(255) not null,
review varchar(255) not null,
status varchar(255) not null,
primary key (UserID,PaperID));