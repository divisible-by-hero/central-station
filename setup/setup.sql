SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_authentication_groups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_authentication_groups` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_authentication_groups` (
  `id` MEDIUMINT(8) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(20) NOT NULL ,
  `description` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_authentication`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_authentication` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_authentication` (
  `id` MEDIUMINT(8) NOT NULL AUTO_INCREMENT ,
  `group_id` MEDIUMINT(8) NOT NULL COMMENT '					' ,
  `ip_address` CHAR(16) NOT NULL ,
  `username` VARCHAR(15) NOT NULL ,
  `password` VARCHAR(40) NOT NULL ,
  `salt` VARCHAR(40) NULL ,
  `email` VARCHAR(100) NOT NULL ,
  `activation_code` VARCHAR(40) NULL ,
  `forgotten_password_code` VARCHAR(40) NULL ,
  `remember_code` VARCHAR(40) NULL ,
  `created_on` INT(11) NOT NULL ,
  `last_login` INT(11) NULL ,
  `active` TINYINT(1) NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `group_id`
    FOREIGN KEY (`group_id` )
    REFERENCES `defectTracker`.`defect_authentication_groups` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `group_id` ON `defectTracker`.`defect_authentication` (`group_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_project`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_project` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_project` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(255) NOT NULL ,
  `date_created` DATE NOT NULL ,
  `author_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `author_id`
    FOREIGN KEY (`author_id` )
    REFERENCES `defectTracker`.`defect_authentication` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `author_id` ON `defectTracker`.`defect_project` (`author_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_defect_severity`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_defect_severity` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_defect_severity` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `severity` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_defect_state`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_defect_state` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_defect_state` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `state` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_defect`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_defect` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_defect` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(255) NOT NULL ,
  `description` LONGBLOB NULL ,
  `project_id` INT NOT NULL ,
  `severity_id` INT NOT NULL ,
  `state_id` INT NOT NULL ,
  `date_created` DATE NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `project_id`
    FOREIGN KEY (`project_id` )
    REFERENCES `defectTracker`.`defect_project` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `severity_id`
    FOREIGN KEY (`severity_id` )
    REFERENCES `defectTracker`.`defect_defect_severity` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `state_id`
    FOREIGN KEY (`state_id` )
    REFERENCES `defectTracker`.`defect_defect_state` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `project_id` ON `defectTracker`.`defect_defect` (`project_id` ASC) ;

CREATE INDEX `severity_id` ON `defectTracker`.`defect_defect` (`severity_id` ASC) ;

CREATE INDEX `state_id` ON `defectTracker`.`defect_defect` (`state_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_project_version`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_project_version` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_project_version` (
  `id` INT NOT NULL ,
  `project_id` INT NOT NULL ,
  `version_number` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `project_id`
    FOREIGN KEY (`project_id` )
    REFERENCES `defectTracker`.`defect_project` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `project_id` ON `defectTracker`.`defect_project_version` (`project_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_forum`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_forum` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_forum` (
  `id` INT NOT NULL ,
  `title` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_forum_board`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_forum_board` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_forum_board` (
  `id` INT NOT NULL ,
  `title` VARCHAR(255) NULL ,
  `project_id` INT NULL ,
  `forum_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `project_id`
    FOREIGN KEY (`project_id` )
    REFERENCES `defectTracker`.`defect_project` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `forum_id`
    FOREIGN KEY (`forum_id` )
    REFERENCES `defectTracker`.`defect_forum` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `project_id` ON `defectTracker`.`defect_forum_board` (`project_id` ASC) ;

CREATE INDEX `forum_id` ON `defectTracker`.`defect_forum_board` (`forum_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_forum_post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_forum_post` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_forum_post` (
  `id` INT NOT NULL ,
  `title` VARCHAR(255) NULL ,
  `content` LONGBLOB NULL ,
  `author_id` INT NULL ,
  `board_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `author_id`
    FOREIGN KEY (`author_id` )
    REFERENCES `defectTracker`.`defect_authentication` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `board_id`
    FOREIGN KEY (`board_id` )
    REFERENCES `defectTracker`.`defect_forum_board` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `author_id` ON `defectTracker`.`defect_forum_post` (`author_id` ASC) ;

CREATE INDEX `board_id` ON `defectTracker`.`defect_forum_post` (`board_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_comments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_comments` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_comments` (
  `id` INT NOT NULL ,
  `defect_id` INT NOT NULL ,
  `author_id` INT NOT NULL ,
  `comment` LONGBLOB NULL ,
  `date_created` DATE NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `defect_id`
    FOREIGN KEY (`defect_id` )
    REFERENCES `defectTracker`.`defect_defect` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `author_id`
    FOREIGN KEY (`author_id` )
    REFERENCES `defectTracker`.`defect_authentication` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `defect_id` ON `defectTracker`.`defect_comments` (`defect_id` ASC) ;

CREATE INDEX `author_id` ON `defectTracker`.`defect_comments` (`author_id` ASC) ;


-- -----------------------------------------------------
-- Table `defectTracker`.`defect_authentication_meta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `defectTracker`.`defect_authentication_meta` ;

CREATE  TABLE IF NOT EXISTS `defectTracker`.`defect_authentication_meta` (
  `id` MEDIUMINT(8) NOT NULL AUTO_INCREMENT ,
  `user_id` MEDIUMINT(8) NOT NULL ,
  `first_name` VARCHAR(50) NULL ,
  `last_name` VARCHAR(50) NULL ,
  `company` VARCHAR(100) NULL ,
  `phone` VARCHAR(20) NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id` )
    REFERENCES `defectTracker`.`defect_authentication` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `user_id` ON `defectTracker`.`defect_authentication_meta` (`user_id` ASC) ;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
