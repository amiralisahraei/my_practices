// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.3;

contract Mycontract {

    string value;
    bool passed;
    int num;
    address My_add;
    bytes32 [] public names;

    constructor() {
        value = "Myvalue";
        // names = [bytes32("ffffffffffffffffffffffffffffffff"), bytes32("reza"), bytes32("saeid")];
    }

    function get() public view returns(string memory){
        return value;
    }

    function set(string memory _value) public {
        // require(_value > 40, "The number must be bigger than 40");
        value = _value;
    } 

    function get_names() public view returns(bytes32[] memory){
        return names;
    }

}