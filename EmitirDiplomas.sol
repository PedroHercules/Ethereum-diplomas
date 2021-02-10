//SPDX-License-Identifier: UNLICENSED
pragma solidity 0.7.1;

contract EmitirDiploma{
    
    address payable dono;
    constructor() {
        dono = msg.sender;
    }
    
    struct Diploma{
        string discente;
        string dataNasc;
        string curso;
        string conclusao;
        string cidade;
        string iesEmissora;
        uint rgDiscente;
    }
    
    Diploma diploma;
    
    modifier onlyOwner(address conta_acesso){
        require(dono == conta_acesso);
        _;
    }
    
    function transferEther() external payable{
        dono.transfer(msg.value);
    }
    
    function registrarDiploma(string memory _discente, string memory _dataNasc, string memory _curso, string memory _conclusao,
     string memory _cidade, string memory _iesEmissora, uint _rgDiscente) public onlyOwner(msg.sender){
        diploma = Diploma (
            {
                discente: _discente,
                dataNasc: _dataNasc,
                curso: _curso,
                conclusao: _conclusao,
                iesEmissora: _iesEmissora,
                cidade: _cidade,
                rgDiscente: _rgDiscente
            }
        );
    }
}