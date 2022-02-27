/*
 Navicat Premium Data Transfer

 Source Server         : student_system
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : db_student

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 13/11/2021 23:31:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_class
-- ----------------------------
DROP TABLE IF EXISTS `tb_class`;
CREATE TABLE `tb_class`  (
  `classID` int NOT NULL,
  `gradeID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `className` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`classID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_class
-- ----------------------------
INSERT INTO `tb_class` VALUES (1, '高一', '五班');
INSERT INTO `tb_class` VALUES (2, '初二', '三班');

-- ----------------------------
-- Table structure for tb_examkinds
-- ----------------------------
DROP TABLE IF EXISTS `tb_examkinds`;
CREATE TABLE `tb_examkinds`  (
  `kindID` int NOT NULL,
  `kindName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`kindID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_examkinds
-- ----------------------------
INSERT INTO `tb_examkinds` VALUES (1, '第一次月考');
INSERT INTO `tb_examkinds` VALUES (2, '期中考试');
INSERT INTO `tb_examkinds` VALUES (3, '第二次月考');
INSERT INTO `tb_examkinds` VALUES (4, '期末考试');

-- ----------------------------
-- Table structure for tb_grade
-- ----------------------------
DROP TABLE IF EXISTS `tb_grade`;
CREATE TABLE `tb_grade`  (
  `gradeID` int NOT NULL,
  `gradeName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`gradeID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_grade
-- ----------------------------
INSERT INTO `tb_grade` VALUES (1, '高三');
INSERT INTO `tb_grade` VALUES (2, '高二');
INSERT INTO `tb_grade` VALUES (4, '高一');
INSERT INTO `tb_grade` VALUES (5, '初一');
INSERT INTO `tb_grade` VALUES (6, '初二');

-- ----------------------------
-- Table structure for tb_result
-- ----------------------------
DROP TABLE IF EXISTS `tb_result`;
CREATE TABLE `tb_result`  (
  `ID` int NOT NULL AUTO_INCREMENT COMMENT '自动编号',
  `stuID` int NOT NULL COMMENT '学生编号',
  `kindID` int NOT NULL COMMENT '考试类别编号',
  `subID` int NOT NULL COMMENT '考试科目编号',
  `result` double NOT NULL COMMENT '考试成绩',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_result
-- ----------------------------
INSERT INTO `tb_result` VALUES (4, 1120212707, 1, 1, 139);
INSERT INTO `tb_result` VALUES (5, 1120212707, 1, 1, 143);

-- ----------------------------
-- Table structure for tb_student
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student`  (
  `stuID` int NOT NULL COMMENT '学生编号',
  `stuName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学生姓名',
  `classID` int NOT NULL COMMENT '班级编号',
  `gradeID` int NOT NULL COMMENT '年级编号',
  `age` int NOT NULL COMMENT '年龄',
  `sex` char(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '性别',
  `phone` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '联系电话',
  `address` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '家庭住址',
  PRIMARY KEY (`stuID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_student
-- ----------------------------
INSERT INTO `tb_student` VALUES (1120212298, '王麻子', 1, 2, 18, '男', '13987673365', '吉林省长春市');
INSERT INTO `tb_student` VALUES (1120212707, '李四', 1, 4, 19, '女', '13881466189', '北京市海淀');
INSERT INTO `tb_student` VALUES (1120212876, '王飞', 1, 1, 20, '女', '13987655521', '四川省成都市');

-- ----------------------------
-- Table structure for tb_subject
-- ----------------------------
DROP TABLE IF EXISTS `tb_subject`;
CREATE TABLE `tb_subject`  (
  `subID` int NOT NULL COMMENT '科目编号',
  `subName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '科目名称',
  PRIMARY KEY (`subID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_subject
-- ----------------------------
INSERT INTO `tb_subject` VALUES (1, '数学');
INSERT INTO `tb_subject` VALUES (2, '语文');
INSERT INTO `tb_subject` VALUES (4, '物理');
INSERT INTO `tb_subject` VALUES (5, '化学');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user`  (
  `userName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户姓名',
  `userPwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户密码',
  PRIMARY KEY (`userName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('LHC', '123456');
INSERT INTO `tb_user` VALUES ('LHY', '12345678');
INSERT INTO `tb_user` VALUES ('wdsj', '098988');

-- ----------------------------
-- View structure for v_classinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_classinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName`,`tb_class`.`className` AS `className` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`);

-- ----------------------------
-- View structure for v_resultinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_resultinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_resultinfo` AS select `tb_result`.`ID` AS `ID`,`tb_result`.`stuID` AS `stuID`,`tb_examkinds`.`kindName` AS `kindName`,`tb_subject`.`subName` AS `subName`,`v_studentinfo`.`className` AS `className`,`v_studentinfo`.`gradeName` AS `gradeName`,`tb_result`.`result` AS `result`,`v_studentinfo`.`stuName` AS `stuName` from (((`tb_subject` join `tb_result`) join `tb_examkinds`) join `v_studentinfo`) where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and (`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and (`tb_result`.`subID` = `tb_subject`.`subID`));

-- ----------------------------
-- View structure for v_studentinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_studentinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`sex` AS `sex`,`tb_student`.`age` AS `age`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`));

SET FOREIGN_KEY_CHECKS = 1;
