-- MySQL dump 10.13  Distrib 5.7.12, for Linux (x86_64)
--
-- Host: 123.57.55.229    Database: spbroadcast
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add group',7,'add_group'),(20,'Can change group',7,'change_group'),(21,'Can delete group',7,'delete_group'),(22,'Can add presenter',8,'add_presenter'),(23,'Can change presenter',8,'change_presenter'),(24,'Can delete presenter',8,'delete_presenter'),(25,'Can add spnews',9,'add_spnews'),(26,'Can change spnews',9,'change_spnews'),(27,'Can delete spnews',9,'delete_spnews'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add banner',11,'add_banner'),(32,'Can change banner',11,'change_banner'),(33,'Can delete banner',11,'delete_banner'),(34,'Can add fengmian',12,'add_fengmian'),(35,'Can change fengmian',12,'change_fengmian'),(36,'Can delete fengmian',12,'delete_fengmian'),(37,'Can add shipin',13,'add_shipin'),(38,'Can change shipin',13,'change_shipin'),(39,'Can delete shipin',13,'delete_shipin');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$schKuASmfmGH$I+FPhVGDehUgbBHtcqMwOm0OA2zGPallVvYhLJi42Mc=','2016-03-25 08:24:54',1,'cat','','','418435432@qq.com',1,1,'2016-03-25 08:18:32');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banner`
--

DROP TABLE IF EXISTS `banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `desc` varchar(45) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `image_path` varchar(145) DEFAULT NULL,
  `uri` varchar(245) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner`
--

LOCK TABLES `banner` WRITE;
/*!40000 ALTER TABLE `banner` DISABLE KEYS */;
INSERT INTO `banner` VALUES (1,'第一个ｂａｎｎｅｒ','hhhh','2016-04-09 22:40:25','banner_banner1.png','http://www.baidu.com',1),(2,'bb','','2016-04-09 22:49:51','banner_banner0.png','http://www.163.com',-1),(3,'dd你好','','2016-04-09 22:59:42','banner_banner1.png','http://www.qq.com',1),(4,'测试','新浪','2016-04-15 17:23:52','banner_1460712232.95_104-160113145422513.jpg','http://www.sina.com.cn',1);
/*!40000 ALTER TABLE `banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'index','group'),(8,'index','presenter'),(9,'index','spnews'),(10,'index','user'),(11,'index','banner'),(12,'index','fengmian'),(13,'index','shipin');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-03-25 08:18:13'),(2,'auth','0001_initial','2016-03-25 08:18:13'),(3,'admin','0001_initial','2016-03-25 08:18:13'),(4,'contenttypes','0002_remove_content_type_name','2016-03-25 08:18:14'),(5,'auth','0002_alter_permission_name_max_length','2016-03-25 08:18:14'),(6,'auth','0003_alter_user_email_max_length','2016-03-25 08:18:14'),(7,'auth','0004_alter_user_username_opts','2016-03-25 08:18:14'),(8,'auth','0005_alter_user_last_login_null','2016-03-25 08:18:14'),(9,'auth','0006_require_contenttypes_0002','2016-03-25 08:18:14'),(10,'sessions','0001_initial','2016-03-25 08:18:14');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9a14ysvyg8gdap2095t2e7itlu3r1yth','MjZiZDFjMGEwYWFhMzI0NDRhOWQ3MGE2MjNiYjhlOTYxMzAxMTBkZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY3OTU2MjE4MWM3MDEzNzFkYjk1MTdmOWU2NGZmMTRlZjVkYTFiMGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-04-08 08:24:55'),('k7wieqjk6nkv03jtqkuozfdl5p893fp3','ZGVkMzQ0YWUyMTM0NWRmODU4ZDFmZGE4NjI1N2QwMjViYzE3MzQxZDp7InVzZXJpbmZvIjp7InVzZXJuYW1lIjoiYSIsInJpZ2h0IjoxMCwibmlja25hbWUiOm51bGwsInNleCI6bnVsbH19','2016-04-28 13:37:11');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fengmian`
--

DROP TABLE IF EXISTS `fengmian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fengmian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(145) DEFAULT NULL,
  `path` varchar(145) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `desc` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fengmian`
--

LOCK TABLES `fengmian` WRITE;
/*!40000 ALTER TABLE `fengmian` DISABLE KEYS */;
INSERT INTO `fengmian` VALUES (1,'路飞','fengmian_IMG_20160224_101517R.jpg',0,'2016-04-09 21:46:08','2016-04-09 21:46:08','路飞'),(2,'索隆','fengmian_IMG_20160224_100340R.jpg',0,'2016-04-09 22:02:52','2016-04-09 22:02:52','哈哈哈');
/*!40000 ALTER TABLE `fengmian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(100) NOT NULL,
  `groupright` int(11) NOT NULL,
  `desc` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `huodong`
--

DROP TABLE IF EXISTS `huodong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `huodong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(245) DEFAULT NULL,
  `content` text,
  `starttime` varchar(20) DEFAULT NULL,
  `endtime` varchar(20) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `author` varchar(145) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `huodong`
--

LOCK TABLES `huodong` WRITE;
/*!40000 ALTER TABLE `huodong` DISABLE KEYS */;
INSERT INTO `huodong` VALUES (1,'加菲小小小猫','<p>撒旦发送</p>','1980-05-14','1980-05-13',2,'cooler','2016-04-13 15:08:24','2016-04-13 15:08:24'),(2,'加菲小小小猫','<p>撒旦发送</p>','1980-05-14','1980-05-13',-1,'cooler','2016-04-13 15:08:32','2016-04-13 15:08:32'),(3,'asdf ','<p>sadfaas</p><p>fdgdsafdsaf&nbsp;</p>','2016-04-13','2016-04-13',1,'adsfaf','2016-04-13 15:10:08','2016-04-13 15:10:08'),(4,'adfdaf','<p>asdgaga&nbsp;</p>','2016-04-14','2016-04-22',1,'adsfasf ','2016-04-13 15:10:49','2016-04-13 15:10:49'),(5,'第一个','<div class=\"rule-item\">\n			<h2>活动引言</h2>\n			<p  class=\"infos\">\n				\"点赞吉林·弘扬社会正能量\"手机摄影 大赛，由吉林省互联网信息办公室、共青团吉林省委、吉林日报社主办，吉林日报社群众工作部协助活动比赛。\n			</p>\n		</div>\n		<div class=\"rule-item\">\n			<h2>活动目的</h2>\n			<p  class=\"infos\">\n				随着智能手机功能和应用的快速发展，摄影爱好者们可以随时、随地、随手抓拍到生活中更多的美与感动。本次大赛以“点赞吉林，弘扬社会正能量”为主题、以 “展示吉林风采，抓住感动瞬间，记录百姓生活，传递爱与关怀”为主要目的， 面向全社会征集手机摄影作品，旨在唱响网络主旋律、传递网络正能量，弘扬社会主义核心价值观。\n			</p>\n		</div>\n		<div class=\"rule-item\">\n			<h2>活动规则</h2>\n			<dl class=\"clearfix\">\n				<dt>一</dt>\n				<dd>\n					作品要求\n					<br/>\n					参赛作品内容要求积极健康，每人最多提交3幅作品，作品形式为单幅作品或者组照（组照照片总数不超过3张） ；\n				</dd>\n				<dt>二</dt>\n				<dd>\n					本次大赛不接受数码相机拍摄和胶片相机扫描件文件，不接受手机全画幅拍摄作品以及纸质作品投稿。作品电子格式必须为JPG文件，照片可以进行裁剪、旋转、色彩等简单处理，但禁止使用photoshop等软件进行任何深度处理。作品需保留EXIF信息，便于组委会查看。\n				</dd>\n				<dt>三</dt>\n				<dd>\n					参赛者应保证为作品的原创作者，并对该作品的整体及局部均拥有独立、完整、明确、无争议的著作权；参赛者还应保证其所投送的作品不侵犯第三人的著作权、肖像权、名誉权、隐私权等在内的合法权益。\n				</dd>\n\n				<dt>四</dt>\n				<dd>对于入选作品，主办单位有权以复制、发行、展览、放映、信息网络传播等方式使用，并可不支付报酬。</dd>\n				<dt>五</dt>\n				<dd>5.本届手机摄影大赛及征稿启事解释权属于主办单位。参赛者一经投稿，即视为其已同意本征稿启事之所有规定。</dd>\n\n				<dt>六</dt>\n				<dd>\n					作品类别\n					<br/>\n					以“弘扬社会正能量”为主题，选手根据作品的特点按照“点滴生活”、“爱与感动”、“美丽校园”、“大美吉林”、“创享美拍”五方面投放作品。\n				</dd>\n			</dl>\n		</div>\n		<div class=\"rule-item\">\n			<h2>活动时间</h2>\n			<div class=\"time-list clearfix\">\n				<ul>\n					<li>\n						<img src=\"/static/style/imgs/xuhao.jpg\"/>\n						<span class=\"tit\">报名投稿</span>\n						<span class=\"date\">2015.10.15~2015.11.15</span>\n					</li>\n					<li>\n						<img src=\"/static/style/imgs/xuhao.jpg\"/>\n						<span class=\"tit\">作品整理及初选</span>\n						<span class=\"date\">2015.10.15~2015.11.15</span>\n					</li>\n					<li>\n						<img src=\"/static/style/imgs/xuhao.jpg\"/>\n						<span class=\"tit\">网络投票</span>\n						<span class=\"date\">2015.10.15~2015.11.15</span>\n					</li>\n					<li>\n						<img src=\"/static/style/imgs/xuhao.jpg\"/>\n						<span class=\"tit\">颁奖巡演</span>\n						<span class=\"date\">2015.10.15~2015.11.15</span>\n					</li>\n				</ul>\n			</div>\n		</div>\n\n		<div class=\"rule-item\">\n			<h2>投稿方式</h2>\n			<div class=\"commit-form\">\n				<img class=\"erweima\" src=\"/static/style/imgs/erweima.jpg\"/>\n				<div class=\"text clearfix\">\n					<p>参与者可以通过扫描二维码和微信平台主动添加的方式关注“吉报教育在线”微信公共平台了解活动详情，并进行活动投稿和投票</p>\n					<dl>\n						<dt>1、</dt>\n						<dd>手机投稿：发送“我要参赛+姓名+手机号码+作品名称”及参赛作品至“吉报教育在线”微信公众平台；</dd>\n						<dt>2、</dt>\n						<dd>\n							邮箱投稿：将邮件主题及作品附件命名为“姓名+手机号码+作品名称”发送至邮箱：sjsheyingdasai@163.com。\n						</dd>\n					</dl>\n				</div>\n			</div>\n		</div>\n		<div class=\"rule-item\">\n			<h2>比赛奖励</h2>\n			<div class=\"reward clearfix\">\n				<div class=\"box\">\n					<img src=\"/static/style/imgs/reward.png\"/>\n					<span class=\"level\">一等奖(1名)</span>\n					<span class=\"info\">华为Mate S 手机一部</span>\n				</div>\n				<div class=\"box\">\n					<img src=\"/static/style/imgs/reward.png\"/>\n					<span class=\"level\">二等奖(3名)</span>\n					<span class=\"info\">华为Mate 7 手机一部</span>\n				</div>\n				<div class=\"box end\">\n					<img src=\"/static/style/imgs/reward.png\"/>\n					<span class=\"level\">三等奖(10名)</span>\n					<span class=\"info\">华为荣耀6 手机一部</span>\n				</div>\n				<div class=\"box\">\n					<img src=\"/static/style/imgs/reward.png\"/>\n					<span class=\"level\">优秀奖(50名)</span>\n					<span class=\"info\">华为便携式音响一台</span>\n				</div>\n				<div class=\"box\">\n					<img src=\"/static/style/imgs/reward.png\"/>\n					<span class=\"level\">参与奖</span>\n					<span class=\"info\">有机会获得话费50元</span>\n				</div>\n			</div>\n		</div>\n\n		<div class=\"rule-item\">\n			<h2>主办单位</h2>\n			<div class=\"sponser\">\n				<p>主办单位:吉林省互联网信息办公室、共青团吉林省委、吉林日报社</p>\n				<p>协办单位：吉林日报社群众工作部</p>\n			</div>\n		</div>','2016-04-13','2016-04-28',1,'cooler','2016-04-13 18:14:38','2016-04-13 18:14:38');
/*!40000 ALTER TABLE `huodong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presenter`
--

DROP TABLE IF EXISTS `presenter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presenter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) DEFAULT NULL,
  `birthday` datetime DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `department` varchar(145) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `head_image` varchar(145) NOT NULL,
  `abstract` longtext,
  `title` varchar(145) DEFAULT NULL,
  `read_num` int(11) DEFAULT NULL,
  `zan_num` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `ntype` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presenter`
--

LOCK TABLES `presenter` WRITE;
/*!40000 ALTER TABLE `presenter` DISABLE KEYS */;
INSERT INTO `presenter` VALUES (1,'ddd',NULL,1,'的撒发送','2016-04-12 19:13:35','2016-04-12 19:13:35','presenter_presenter.png','的撒发大发','答复的',0,0,0,0),(2,'加菲小小小猫',NULL,1,'电视主持人','2016-04-12 19:14:51','2016-04-12 19:14:51','presenter_presenter.png','的撒发大发','主任',0,0,0,0),(3,'加菲小小小猫',NULL,0,'电视主持人','2016-04-12 19:17:45','2016-04-12 19:17:45','presenter_1460459865.63_presenter.png','阿斯顿发大水噶大使馆','主任',0,0,0,0),(4,'朱军',NULL,0,'电视主持人','2016-04-12 22:04:44','2016-04-12 22:04:44','presenter_1460469884.43_presenter.png','阿斯顿发大水噶大使馆','主任',0,0,0,0),(5,'加菲小小小猫',NULL,1,'电视主持人','2016-04-12 22:05:03','2016-04-12 22:05:03','presenter_1460469903.87_presenter-1.png','的撒发大发','主任',0,0,0,0);
/*!40000 ALTER TABLE `presenter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipin`
--

DROP TABLE IF EXISTS `shipin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shipin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(145) DEFAULT NULL,
  `path` varchar(145) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `desc` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipin`
--

LOCK TABLES `shipin` WRITE;
/*!40000 ALTER TABLE `shipin` DISABLE KEYS */;
INSERT INTO `shipin` VALUES (1,'路飞','shipin_cooler.mp4',0,'2016-04-09 21:50:53','2016-04-09 21:50:53','路飞'),(2,'主任','shipin_22.mp4',0,'2016-04-09 22:04:18','2016-04-09 22:04:18','索隆啊啊啊'),(3,'dd你好','shipin_1460474900.92_cooler.mp4',0,'2016-04-12 23:28:20','2016-04-12 23:28:20','sadfasfasgdasga');
/*!40000 ALTER TABLE `shipin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splogo`
--

DROP TABLE IF EXISTS `splogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splogo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) DEFAULT NULL,
  `path` varchar(145) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `desc` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splogo`
--

LOCK TABLES `splogo` WRITE;
/*!40000 ALTER TABLE `splogo` DISABLE KEYS */;
INSERT INTO `splogo` VALUES (1,'siping','logo_1461673293.04_IMG_20160224_101546R.jpg',2,'2016-04-26 20:21:33','sadaf'),(2,'sdafa','logo_1461674868.09_IMG_20160224_101522R.jpg',2,'2016-04-26 20:47:48','adsfaf');
/*!40000 ALTER TABLE `splogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spnews`
--

DROP TABLE IF EXISTS `spnews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spnews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `shot_content` varchar(200) DEFAULT NULL,
  `content` longtext,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `read_num` int(11) DEFAULT NULL,
  `zan_num` int(11) DEFAULT NULL,
  `author` varchar(145) DEFAULT NULL,
  `src` varchar(145) DEFAULT NULL,
  `reporter` varchar(145) DEFAULT NULL,
  `desc` varchar(145) DEFAULT NULL,
  `image_media_path` varchar(255) NOT NULL,
  `media_path` varchar(255) NOT NULL,
  `ntype` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `tags` varchar(45) DEFAULT NULL,
  `zebian` varchar(145) DEFAULT NULL,
  `huodongid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=88 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spnews`
--

LOCK TABLES `spnews` WRITE;
/*!40000 ALTER TABLE `spnews` DISABLE KEYS */;
INSERT INTO `spnews` VALUES (1,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 21:51:45','2016-04-09 21:51:45',11,1,'cooler','四平广播电视台','cooler','cooler','fengmian_IMG_20160224_101517R.jpg','shipin_cooler.mp4',1,1,'cooler','None',NULL),(2,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',7,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(3,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(4,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(5,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(6,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(7,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(8,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 22:07:07','2016-04-09 22:07:07',1,1,'猫先生','四平广播电视台','毛','单独','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'单独','None',NULL),(9,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:51:34','2016-04-09 23:51:34',1,1,'周小猫','四平广播电视台','加菲','撒旦发放','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',2,1,'猫','猫',NULL),(10,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',3,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',2,1,'cooler','',NULL),(11,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',2,1,'cooler','',NULL),(12,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',2,1,'cooler','',NULL),(13,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',2,1,'cooler','',NULL),(14,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',NULL),(15,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',NULL),(16,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',6,3,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(17,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,2,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(18,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(19,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(20,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(21,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(22,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(23,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(24,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(25,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',3,1,'cooler','',5),(26,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(27,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(28,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(29,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(30,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(31,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(32,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(33,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(34,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(35,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(36,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(37,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(38,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',3,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(39,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',8,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',4,1,'cooler','',5),(40,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',3,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(41,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(42,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(43,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(44,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(45,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(46,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(47,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(48,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(49,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(50,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(51,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(52,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(53,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(54,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(55,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',5,1,'cooler','',NULL),(56,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(57,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(58,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(59,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(60,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(61,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(62,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(63,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(64,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(65,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(66,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(67,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(68,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(69,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(70,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',6,1,'cooler','',NULL),(71,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(72,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(73,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(74,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(75,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(76,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(77,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(78,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',30,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(79,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(80,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(81,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',1,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(82,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(83,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',2,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(84,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',13,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(85,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-09 23:52:16','2016-04-09 23:52:16',7,1,'cooler','四平广播电视台','cooler','','fengmian_IMG_20160224_100340R.jpg','shipin_22.mp4',1,1,'cooler','',NULL),(86,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-12 23:28:58','2016-04-12 23:28:58',31,1,'cooler','四平广播电视台','cooler','asdfas','fengmian_IMG_20160224_100340R.jpg','shipin_1460474900.92_cooler.mp4',1,1,'asda','sad',NULL),(87,'王宇到二次洪水改造工程现场办公','近日副市长王宇带领市直相关部门负责统治，来到二次洪水改造工程线程进行现场办公，解决工程存在问题，加快工程建设','在全市城区环境综合整治“百日会战”中，市公安局巡警、交警及城管治安监察支队干警首当其冲，克服重重困难，不断加大联合执法力度，使全市城区道路环境和交通秩序得到明显改善。\n','2016-04-13 16:23:17','2016-04-13 16:23:17',9,1,'cooler','四平广播电视台','大沙发发','路飞','fengmian_IMG_20160224_100340R.jpg','shipin_1460474900.92_cooler.mp4',1,1,'撒旦法','啊三大发顺丰',4);
/*!40000 ALTER TABLE `spnews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `toupiaoyanzheng`
--

DROP TABLE IF EXISTS `toupiaoyanzheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `toupiaoyanzheng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `huodongid` int(11) DEFAULT NULL,
  `spnewsid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `ip` varchar(145) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `tptime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toupiaoyanzheng`
--

LOCK TABLES `toupiaoyanzheng` WRITE;
/*!40000 ALTER TABLE `toupiaoyanzheng` DISABLE KEYS */;
INSERT INTO `toupiaoyanzheng` VALUES (1,4,87,NULL,'127.0.0.1','2016-04-13 10:07:54',NULL,NULL),(2,5,38,NULL,'127.0.0.1','2016-04-13 10:18:29',NULL,NULL),(3,5,16,NULL,'127.0.0.1','2016-04-13 10:18:41',NULL,NULL),(4,5,17,NULL,'127.0.0.1','2016-04-13 10:19:48',NULL,NULL),(5,5,16,NULL,'175.25.242.67','2016-04-15 09:21:43',NULL,NULL),(6,5,16,NULL,'58.244.238.130','2016-04-15 09:34:11',NULL,NULL);
/*!40000 ALTER TABLE `toupiaoyanzheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `right` int(11) DEFAULT NULL,
  `groupid` int(11) DEFAULT NULL,
  `real_name` varchar(45) DEFAULT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  `cellphone` varchar(45) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `nickname` varchar(45) DEFAULT NULL,
  `idcard` varchar(45) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `lastmodify` datetime DEFAULT NULL,
  `verify_code` varchar(45) DEFAULT NULL,
  `addip` varchar(45) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `email` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'a','0b4e7a0e5fe84ad35fb5f95b9ceeac79',10,NULL,NULL,NULL,'13548617117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'admin@qq.com'),(2,'cc','0b4e7a0e5fe84ad35fb5f95b9ceeac79',10,NULL,NULL,NULL,'12345678901',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'admin@ww.cn'),(3,'cooler1217','e09c80c42fda55f9d992e59ca6b3307d',10,NULL,NULL,NULL,'15643245678',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'admin@ww.cnd');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-29 16:33:00
