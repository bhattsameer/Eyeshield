# database details

Mysql Database

```
  CREATE DATABASE eyeshield;
  
  USE eyeshield;
  
  CREATE TABLE data(id INT(11) AUTO_INCREMENT PRIMARY KEY, word VARCHAR(3), filename VARCHAR(50));
  
  INSERT INTO data(word,filename) VALUES('A','A.wav');
  INSERT INTO data(word,filename) VALUES('B','B.wav');
  INSERT INTO data(word,filename) VALUES('C','C.wav');
'''
