import Web3Modal from "web3modal";
import {ethers} from "ethers";
import React, { useState, useEffect } from 'react';
import './App.css';
import './index.css'    

const providerOptions = {

}

function Wallet(){
    async function connectWallet(){
        try{
            let web3Modal = new Web3Modal({
                CacheProvider : false,
                providerOptions
            });
            const web3ModalInstance = await web3Modal.connect();
            const web3ModalProvider = new ethers.providers.web3Provider(web3ModalInstance);
            console.log("Web3 Modal Provider", web3ModalProvider);
        }catch(error){
            console.error(error);
        }
    }
    return(
            <button className="btn" onClick={connectWallet}>Connection to wallet</button>
    )
}

export default Wallet;