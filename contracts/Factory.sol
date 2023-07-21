// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;

/**
 * @title Factory
 * @dev Factory Smart Contract
 */

import "./Pool.sol";

contract Factory {


    address owner;

    constructor () {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    Pool pool;
    Pool[] public pools;


    function createPool(string memory _question, string[] memory _proposals, string memory _img, string memory _link) public  {
        pool = new Pool(_question, _proposals,_img, _link);
        pools.push(pool);

    }

    function getquestion(uint _id) public view returns(uint) {
        Pool poolin = pools[_id];
        return poolin.GetQuestion();

    }

    function addvoter (uint _id, address[] memory _voters) public {
        Pool poolin = pools[_id];
        
        for (uint i=0; i < _voters.length; i++){
            poolin.addVoter(_voters[i]);
        }
    
 
    }

    function getwinningproposalname(uint _id) public view returns (string memory winnerName_){
        Pool poolin = pools[_id];
        winnerName_ = poolin.winnerProposalName();
        return winnerName_;
        
    }

    // Function to get the length of the 'pools' array
    function getPoolsLength() public view returns (uint256) {
        return pools.length;
    }


} 