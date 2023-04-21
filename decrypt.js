const CryptoJS = require('crypto-js');

// Get the encrypted string from the command line arguments
const encryptedString = process.argv[3];

// Generate a random key
const key = process.argv[2];

// Decrypt the string using CryptoJS
const decryptedBytes = CryptoJS.AES.decrypt(encryptedString, key);
const decryptedString = decryptedBytes.toString(CryptoJS.enc.Utf8);

// Print the decrypted result
console.log(decryptedString);
