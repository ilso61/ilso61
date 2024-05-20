/*
Created: 01.04.2024
Modified: 08.04.2024
Model: Microsoft SQL Server 2016
Database: MS SQL Server 2016
*/


-- Create tables section -------------------------------------------------

-- Table Entry

CREATE TABLE [Entry]
(
 [id] Int NOT NULL,
 [entry] Ntext NOT NULL
)
go

-- Add keys for table Entry

ALTER TABLE [Entry] ADD CONSTRAINT [PK_Entry] PRIMARY KEY ([id])
go

-- Table Word

CREATE TABLE [Word]
(
 [word] NVarchar(50) NOT NULL,
 [alt_word] NVarchar(50) NULL,
 [id] Int NOT NULL
)
go

-- Add keys for table Word

ALTER TABLE [Word] ADD CONSTRAINT [PK_Word] PRIMARY KEY ([id])
go

-- Table Morphemes

CREATE TABLE [Morphemes]
(
 [morphs] NVarchar(max) NULL,
 [morphs_tags] NVarchar(max) NULL,
 [id] Int NOT NULL
)
go

-- Add keys for table Morphemes

ALTER TABLE [Morphemes] ADD CONSTRAINT [PK_Morphemes] PRIMARY KEY ([id])
go

-- Table Other

CREATE TABLE [Other]
(
 [translation] NVarchar(50) NOT NULL,
 [etymology] NVarchar(5) NULL,
 [part] NVarchar(10) NOT NULL,
 [id] Int NOT NULL
)
go

-- Add keys for table Other

ALTER TABLE [Other] ADD CONSTRAINT [PK_Other] PRIMARY KEY ([id])
go

-- Create foreign keys (relationships) section ------------------------------------------------- 


ALTER TABLE [Other] ADD CONSTRAINT [Entry - Other] FOREIGN KEY ([id]) REFERENCES [Entry] ([id]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [Morphemes] ADD CONSTRAINT [Entry - Morphemes] FOREIGN KEY ([id]) REFERENCES [Entry] ([id]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [Word] ADD CONSTRAINT [Entry - Word] FOREIGN KEY ([id]) REFERENCES [Entry] ([id]) ON UPDATE NO ACTION ON DELETE NO ACTION
go




