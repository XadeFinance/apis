const {
	ethers
} = require('ethers');

require('dotenv').config();

const provider = new ethers.JsonRpcProvider(
	"https://endpoints.omniatech.io/v1/matic/mainnet/public"
);
let contractAbi = [{
	"inputs": [],
	"stateMutability": "nonpayable",
	"type": "constructor"
}, {
	"anonymous": false,
	"inputs": [{
		"indexed": true,
		"internalType": "address",
		"name": "previousOwner",
		"type": "address"
	}, {
		"indexed": true,
		"internalType": "address",
		"name": "newOwner",
		"type": "address"
	}],
	"name": "OwnershipTransferred",
	"type": "event"
}, {
	"inputs": [],
	"name": "owner",
	"outputs": [{
		"internalType": "address",
		"name": "",
		"type": "address"
	}],
	"stateMutability": "view",
	"type": "function"
}, {
	"inputs": [],
	"name": "renounceOwnership",
	"outputs": [],
	"stateMutability": "nonpayable",
	"type": "function"
}, {
	"inputs": [{
		"internalType": "address",
		"name": "newOwner",
		"type": "address"
	}],
	"name": "transferOwnership",
	"outputs": [],
	"stateMutability": "nonpayable",
	"type": "function"
}, {
	"inputs": [{
		"internalType": "address",
		"name": "_to",
		"type": "address"
	}, {
		"internalType": "uint256",
		"name": "_amount",
		"type": "uint256"
	}],
	"name": "transferXUSD",
	"outputs": [],
	"stateMutability": "nonpayable",
	"type": "function"
}, {
	"stateMutability": "payable",
	"type": "receive"
}]
const wallet = new ethers.Wallet(
	process.env.privateKey,
	provider
);

let contract = new ethers.Contract(
	"0x895510D75335DB3c8b1463DD5ffC2d85994E1092",
	contractAbi,
	wallet
);
const recipient = process.argv[2];
const amount = process.argv[3];
async function transfer() {
	let tx = await contract.transferXUSD(
		recipient,
		amount, {
			gasPrice: ethers.parseUnits('400', 'gwei')
		}
	);
	console.log(tx);
}

transfer();
