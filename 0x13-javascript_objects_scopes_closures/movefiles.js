#!/usr/bin/node

const fs = require('fs');
const path = require('path');

const sourceDirectory = './'; // Directory where the files are currently located
const destinationDirectory = './tests'; // Directory where the files will be moved

fs.readdir(sourceDirectory, (error, files) => {
  if (error) {
    console.error('An error occurred while reading the directory:', error);
    return;
  }

  files.forEach((filename) => {
    if (filename.endsWith('main.js')) {
      const sourcePath = path.join(sourceDirectory, filename);
      const destinationPath = path.join(destinationDirectory, filename);

      fs.rename(sourcePath, destinationPath, (error) => {
        if (error) {
          console.error(`An error occurred while moving the file ${filename}:`, error);
        } else {
          console.log(`File ${filename} moved successfully.`);
        }
      });
    }
  });
});
