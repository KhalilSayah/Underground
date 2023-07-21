// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;


contract Pool {

    string public question;

    uint deploy_time;
    uint public start;
    uint public end;
    string public img_ipfs;
    string public link;

    struct Proposal {
        string name;
        uint count;
    }

    struct Voter {
        uint weight; // weight is accumulated by delegation
        bool voted;  // if true, that person already voted
        uint vote_proposal;  // index of the voted proposal
 
    }

    Proposal[] public proposals;

    mapping(address => Voter) public voters;

    modifier timer() {
        require(block.timestamp < end);
        _;
    }


    constructor (string memory _question, string[] memory _proposals, string memory _img, string memory _link){
        question = _question;
        deploy_time = block.timestamp;
        start = block.timestamp;
        end = block.timestamp + 24 hours;
        img_ipfs = _img;
        link = _link;


        for (uint i=0; i < _proposals.length; i++){
            proposals.push(Proposal({
                name: _proposals[i],
                count: 0
            }));
        }
    }

    function addVoter(address _voter) public {
        Voter memory voter = Voter(1,false,0);
        voters[_voter] = voter;
    }


    
    function GetQuestion() public view returns(uint)  {
        return end;
    }




    function vote(uint proposal) public timer {
        require(voters[msg.sender].weight >0, "Cette address n'a pas assez de Weight pour voter");
        proposals[proposal].count += 1;
        voters[msg.sender].weight = 0;
        voters[msg.sender].vote_proposal = proposal;
        voters[msg.sender].voted = true;
    }

    function winningProposal() public view
            returns (uint winningProposal_)
    {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].count > winningVoteCount) {
                winningVoteCount = proposals[p].count;
                winningProposal_ = p;
            }
        }
    }

     
    function winnerProposalName() external view
            returns (string memory winnerName_)
    {
        winnerName_ = proposals[winningProposal()].name;
    }

    function GETwinnerProposal() external view
            returns (Proposal memory winnerP_)
    {
        winnerP_ = proposals[winningProposal()];
    }


     //function return length of proposals
    function getProposalsLength() public view returns (uint256) {
        return proposals.length;
    }

    



}