// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract Voting {
  
  mapping (bytes32 => uint256) public votesReceived;
  //   bytes32 is useful when your words are not more than 32 bytes (32 words) actually they are fixed
  bytes32[] public candidateList;

  constructor(bytes32[] memory candidateNames) {
    candidateList = candidateNames;
  }

  function totalVotesFor(bytes32 candidate) view public returns (uint256) {
    require(validCandidate(candidate));
    return votesReceived[candidate];
  }

  
  function voteForCandidate(bytes32 candidate) public {
    require(validCandidate(candidate));
    votesReceived[candidate] += 1;
  }

  function validCandidate(bytes32 candidate) view public returns (bool) {
    for(uint i = 0; i < candidateList.length; i++) {
      if (candidateList[i] == candidate) {
        return true;
      }
    }
    return false;
  }
}