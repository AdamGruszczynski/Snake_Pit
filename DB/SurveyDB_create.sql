-- Last modification date: 2017-01-27 01:24:18.019

-- tables
-- Table: Clusters
CREATE TABLE Clusters (
    ClusterID integer NOT NULL CONSTRAINT Clusters_pk PRIMARY KEY,
    ClusterNum integer NOT NULL,
    Data text NOT NULL,
    Surveys_SurveyID integer NOT NULL,
    CONSTRAINT Clusters_Surveys FOREIGN KEY (Surveys_SurveyID)
    REFERENCES Surveys (SurveyID)
);

-- Table: Demographic
CREATE TABLE Demographic (
    Users_UserID integer NOT NULL CONSTRAINT Demographic_pk PRIMARY KEY,
    Race text,
    Gender text,
    Age integer,
    Country text,
    City text,
    State text,
    CONSTRAINT Demographic_Users FOREIGN KEY (Users_UserID)
    REFERENCES Users (UserID)
);

-- Table: MemberTypes
CREATE TABLE MemberTypes (
    TypeID integer NOT NULL CONSTRAINT MemberTypes_pk PRIMARY KEY,
    mType text NOT NULL
);

-- Table: Pending
CREATE TABLE Pending (
    Users_UserID integer NOT NULL,
    Surveys_SurveyID integer NOT NULL,
    Expire date NOT NULL,
    CONSTRAINT Pending_pk PRIMARY KEY (Users_UserID,Surveys_SurveyID),
    CONSTRAINT Pending_Surveys FOREIGN KEY (Surveys_SurveyID)
    REFERENCES Surveys (SurveyID),
    CONSTRAINT Pending_Users FOREIGN KEY (Users_UserID)
    REFERENCES Users (UserID)
);

-- Table: Results
CREATE TABLE Results (
    ResultID integer NOT NULL CONSTRAINT Results_pk PRIMARY KEY AUTOINCREMENT,
    Result text NOT NULL,
    Surveys_SurveyID integer NOT NULL,
    Users_UserID integer NOT NULL,
    CONSTRAINT Results_Surveys FOREIGN KEY (Surveys_SurveyID)
    REFERENCES Surveys (SurveyID),
    CONSTRAINT Results_Users FOREIGN KEY (Users_UserID)
    REFERENCES Users (UserID)
);

-- Table: SurveyPrivacy
CREATE TABLE SurveyPrivacy (
    PrivacyID integer NOT NULL CONSTRAINT SurveyPrivacy_pk PRIMARY KEY AUTOINCREMENT,
    pType text NOT NULL
);

-- Table: Survey_Choices
CREATE TABLE SurveyChoices (
    ChoiceID integer NOT NULL CONSTRAINT SurveyChoices_pk PRIMARY KEY AUTOINCREMENT,
    Choice text NOT NULL,
    Surveys_SurveyID integer NOT NULL,
    CONSTRAINT SurveyChoices_Surveys FOREIGN KEY (Surveys_SurveyID)
    REFERENCES Surveys (SurveyID)
);

-- Table: Surveys
CREATE TABLE Surveys (
    SurveyID integer NOT NULL CONSTRAINT Survey_pk PRIMARY KEY AUTOINCREMENT,
    Name text NOT NULL,
    Description text NOT NULL,
    SurveyPrivacy_PrivacyID integer NOT NULL,
    CONSTRAINT Surveys_SurveyPrivacy FOREIGN KEY (SurveyPrivacy_PrivacyID)
    REFERENCES SurveyPrivacy (PrivacyID)
);

-- Table: Users
CREATE TABLE Users (
    UserID integer NOT NULL CONSTRAINT UserInformation_pk PRIMARY KEY AUTOINCREMENT,
    MemberTypes_TypeID integer NOT NULL,
    UserName text NOT NULL,
    Password text NOT NULL,
    CONSTRAINT Users_MemberTypes FOREIGN KEY (MemberTypes_TypeID)
    REFERENCES MemberTypes (TypeID)
);



