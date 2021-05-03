$(document).ready( function(){
    // Log in to window ethereum. 
    const ethEnabled = () => {
      if (window.ethereum) {
        window.web3 = new Web3(window.ethereum);
        window.ethereum.enable();
        return true;
      }
      return false;
    }
    
    // Check whether the environment is OK.
    if (!ethEnabled()) {
      alert("Please install MetaMask to use this dApp!");
    } else {
      console.log("Ethereum!");
    }
    ABI = [
      {
        "constant": true,
        "inputs": [],
        "name": "minter",
        "outputs": [
          {
            "name": "",
            "type": "address"
          }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
      },
      {
        "constant": true,
        "inputs": [
          {
            "name": "",
            "type": "address"
          }
        ],
        "name": "balances",
        "outputs": [
          {
            "name": "",
            "type": "uint256"
          }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [
          {
            "name": "receiver",
            "type": "address"
          },
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "name": "mint",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [],
        "name": "Coin",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [
          {
            "name": "receiver",
            "type": "address"
          },
          {
            "name": "amount",
            "type": "uint256"
          }
        ],
        "name": "send",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"
      },
      {
        "constant": false,
        "inputs": [
          {
            "name": "add",
            "type": "address"
          }
        ],
        "name": "getBalance",
        "outputs": [
          {
            "name": "",
            "type": "uint256"
          }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "anonymous": false,
        "inputs": [
          {
            "indexed": false,
            "name": "from",
            "type": "address"
          },
          {
            "indexed": false,
            "name": "to",
            "type": "address"
          },
          {
            "indexed": false,
            "name": "amount",
            "type": "uint256"
          }
        ],
        "name": "Sent",
        "type": "event"
      }
    ];
    
    window.sender = "0x556C3a1Fc439709CaE2a1795540Cf6094fd3f78F";
    window.SSaddress = "0xD22ABaFA4C81eC8C2f659b17Eb4cC29DdeecEfbb"; 
    window.receiver = "0x8b2701428Aa6169B590B1b08749dd63A5D272456";
    window.myContract = new web3.eth.Contract(ABI, SSaddress);

    function Deposit() {
        console.log("InDeposit");
        DepositTransaction = ({
            from: sender,
            to: SSaddress, // smart contract address
            value: web3.utils.toWei("1", "ether") // 1 Ether = 10^18 Wei
          });
        // Sender's ETH account will reduce 1 ETH and these token will transfer to smart contract (Then Sender's balance will add 1 ETH). 
        myContract.methods.deposit().send(DepositTransaction);
    }
    
    function Send() {
        SendTransaction = ({
            from: sender
        });
        // send 100 Wei from sender. (The balance of sender will subtract 100 Wei and receiver will add 100 Wei)
        myContract.methods.send(receiver, 100).send(SendTransaction);
    }
    
    function Withdraw() {
        WithdrawTransaction = ({
            from: sender
        })
        // Withdraw all tokens
        myContract.methods.getBalance(sender).call().then(function (res) {
          myContract.methods.withdraw(res).send(WithdrawTransaction);
        })
        
    }

    function RefreshBalance() {
        myContract.methods.getBalance(sender).call().then(function (res) {
          // $("#senB").html.  
          console.log(res);
          document.getElementById("senB").innerHTML = web3.utils.fromWei(res);
        })
  
        // myContract.methods.getBalance(receiver).call().then(function (res) {
        //   // $("#senB").html.  
        //   console.log(res);
        //   document.getElementById("recB").innerHTML = web3.utils.fromWei(res);
        // })
      }
    
    // Register in global. Next we need to bind these function to the button.
    window.Deposit = Deposit;
    window.Send = Send;
    window.Withdraw = Withdraw;
    window.RefreshBalance = RefreshBalance;
  }); // <-- close properly
  
  