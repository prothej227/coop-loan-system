BEGIN TRANSACTION;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL,
    `username` VARCHAR(15),
    `email` VARCHAR(50),
    `password` VARCHAR(80),
    PRIMARY KEY(`id`),
    UNIQUE(`username`),
    UNIQUE(`email`)
);

DROP TABLE IF EXISTS `member`;
CREATE TABLE IF NOT EXISTS `member` (
    `member_id` INT NOT NULL,
    `firstName` VARCHAR(255),
    `middleName` VARCHAR(255),
    `lastName` VARCHAR(255),
    `birthAddress` VARCHAR(50),
    `dob` DATE,
    `nationality` VARCHAR(255),
    `religion` VARCHAR(255),
    `sex` VARCHAR(6),
    `civilStatus` VARCHAR(50),
    `curAddress` VARCHAR(255),
    `perAddress` VARCHAR(255),
    `contactNum` VARCHAR(20),
    `zipCode` VARCHAR(10),
    `tinNumber` VARCHAR(40),
    `idType1` VARCHAR(25),
    `idType2` VARCHAR(25),
    `idNumber1` VARCHAR(30),
    `idNumber2` VARCHAR(30),
    `basicEduc` VARCHAR(255),
    `vocDegree` VARCHAR(255),
    `colDegree` VARCHAR(255),
    `posDegree` VARCHAR(255),
    `occupation` VARCHAR(10),
    PRIMARY KEY(`member_id`)
);

DROP TABLE IF EXISTS `beneficiary`;
CREATE TABLE IF NOT EXISTS `beneficiary` (
    `ben_id` INT NOT NULL,
    `member_id` INT,
    `full_name` VARCHAR(255),
    `relationship` VARCHAR(255),
    `dob` DATE,
    `occupation` VARCHAR(255),
    `employer` VARCHAR(255),
    PRIMARY KEY(`ben_id`),
    FOREIGN KEY(`member_id`) REFERENCES `member`(`member_id`)
);

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES (1, 'admin', 'admin@scc.net', 'pbkdf2:sha256:260000$7opijCb07QL9T8lf$47499858abe7d3162c079f43acc63cf8beb99e2582891a7ae021d2b28d4f2968');

INSERT INTO `member` (`member_id`, `firstName`, `middleName`, `lastName`, `birthAddress`, `dob`, `nationality`, `religion`, `sex`, `civilStatus`, `curAddress`, `perAddress`, `contactNum`, `zipCode`, `tinNumber`, `idType1`, `idType2`, `idNumber1`, `idNumber2`, `basicEduc`, `vocDegree`, `colDegree`, `posDegree`, `occupation`) VALUES 
(1, 'Juan', 'Cabigas', 'Cabrillos', 'fsdfsdf', '2024-01-26', 'adasd', 'asdasdas', 'male', NULL, 'sadasd', 'sadasd', 'asdasd', '1111', '1111', 'asdasd', 'saddf', '1111', '1111', 'noEduc', NULL, NULL, NULL, '["PRIV_EMPLOYEE"]'),
(2, 'Journel', 'Cabigas', 'Cabrillos', 'fsdfsdf', '2024-01-03', 'adasd', 'asdasdas', 'male', 'single', 'sadasd', 'sadasd', 'asdasd', '1', '', '', '', '', '', 'noEduc', NULL, NULL, NULL, '[]'),
(3, 'John', 'Smith', 'Doe', '', '2024-01-23', '', '', NULL, NULL, '', '', '', '', '', '', '', '', '', NULL, NULL, NULL, '[]'),
(4, 'Journel', 'Cabigas', 'Cabrillos', 'asddfff', '2024-02-16', '1212', 'dsfdff', 'male', 'single', 'sadasd', NULL, '123433434', '1223423', '122323231', 'asdasd', 'saddf', '122323', '213123', 'elemGrad', NULL, NULL, NULL, '["GOV_EMPLOYEE", "BUSS_PERSON", "HOUSE_WIFE"]'),
(5, 'Journel', 'Cabigas', 'Doe', 'asdasd', '2024-02-10', 'asdff12', 'asdasdas', 'male', 'married', 'sadasd', 'sadasd', 'asdasd', '13242', '65324', 'asdasd', 'asdasd', '1212', '2323', 'hsGrad', 'BS IT', NULL, NULL, '["PRAC_PROFF", "NON_PROFF"]'),
(6, 'Reanne', 'Smith', 'Doe', 'asdasd', '2024-02-08', 'adasd', 'dsfdff', 'female', 'married', 'sadasd', NULL, 'asdasd', '4233', '43434', 'asdasd', 'asdasd', '223', '124', 'elemGrad', NULL, NULL, NULL, '["GOV_EMPLOYEE", "PRIV_EMPLOYEE", "BUSS_PERSON"]'),
(7, 'Journel', 'Cabigas', 'Doe', 'asdasd', '1999-07-22', '1212', 'dsfdff', 'male', 'separated', 'sadasd', 'sadasd', 'asdasd', '43223', '35522', 'asdasd', 'gfhgh', '5645', '5454', 'elemGrad', NULL, NULL, NULL, '["CHUR_SERVANT"]'),
(8, 'Journel', 'Cabigas', 'Doe', 'asdasd', '1999-07-22', '1212', 'asdasdas', 'male', 'single', 'sadasd', 'sadasd', '', '423', '23423', 'asdasd', 'saddf', '1223', '2342', 'elemGrad', NULL, NULL, NULL, '["GOV_EMPLOYEE", "CHUR_SERVANT"]'),
(9, 'John', 'Smith', 'Doe', 'fsdfsdf', '2017-08-11', '1212', 'asdasdas', 'male', 'married', 'sadasd', 'sadasd', 'asdasd', '334', '21213', 'sgfd', 'gggg', '2323', '1212', 'noEduc', NULL, NULL, NULL, '["PRIV_EMPLOYEE", "PRAC_PROFF"]'),
(10, 'asdasd', 'asdasd', 'asdasd', 'asdasdas', '2024-02-08', 'asdasd', 'asdsad', 'female', 'single', 'asdasd', 'asdasd', '13223', '2323', '213123', 'sdfsdf', 'sdfsdf', '2232', '1212', 'elemGrad', NULL, NULL, NULL, '["GOV_EMPLOYEE", "BUSS_PERSON", "OFW", "RET_PEN", "ON"]');

COMMIT;
