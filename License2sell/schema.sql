DROP TABLE IF EXISTS Institute;
DROP TABLE IF EXISTS CodeSource;

CREATE TABLE Institute (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  InstituteName TEXT NOT NULL,
  Certification TEXT NOT NULL,
  DateCertification TIMESTAMP NOT NULL,
  idSource INTEGER,
  CONSTRAINT fk_codeSource,
  FOREIGN KEY (idSource),
  REFERENCES codeSource(idSource),
  UNIQUE(InstituteName, CertificationCode, DateCertification, idSource)
  );
  
  CREATE TABLE CodeSource (
    idSource INTEGER PRIMARY KEY AUTOINCREMENT,
    SourceName TEXT NOT NULL
    );
    
 CREATE UNIQUE INDEX UNQ_InstituteName ON Institute(InstituteName);
