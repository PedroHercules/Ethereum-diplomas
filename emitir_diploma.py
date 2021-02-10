import json
from web3 import Web3, HTTPProvider
 
infura_url = "https://ropsten.infura.io/v3/992c9b04ed7a49539598f4635dbdff0d"
w3 = Web3(HTTPProvider(infura_url))
abi = json.loads('[ { "inputs": [ { "internalType": "string", "name": "_discente", "type": "string" }, { "internalType": "string", "name": "_dataNasc", "type": "string" }, { "internalType": "string", "name": "_curso", "type": "string" }, { "internalType": "string", "name": "_conclusao", "type": "string" }, { "internalType": "string", "name": "_cidade", "type": "string" }, { "internalType": "string", "name": "_iesEmissora", "type": "string" }, { "internalType": "uint256", "name": "_rgDiscente", "type": "uint256" } ], "name": "registrarDiploma", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "transferEther", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" } ]')
address_contract = "0xc891e261d38F7196E0d516141DDa1ee9A2153C93"
contract = w3.eth.contract(address = address_contract, abi = abi)

address_aluno = '0xA42d17320fd5C1779e2a8FA9B92f7Fd29022D76b'
private_key = 'ebc1a9a33cf40afa2390026a6ccf472e945925ee05715f5b0da4b8f30174c62c'
univ_address = '0xbafA8723923B4552a8A86C92d12C8a2f6798e335'
private_key_univ = "a81e5ab035ac82d8319ed233f695225106befe4c8adedb05d1f19ef8c457a636"

discente = "Pedro Hercules de Sousa Dantas"
dataNasc = "07/04/1998"
curso = "Sistemas de Informacao"
conclusao = "20/07/2023"
cidade = "Picos"
iesEmissora = "UFPI"
rgDiscente = 3893056

gas_price = w3.eth.gas_price # Coleta o preço do gas
diploma = contract.functions.registrarDiploma(discente, dataNasc, curso, conclusao, cidade, iesEmissora, rgDiscente) #instancia a função de registrar diploma
diploma_gas = diploma.estimateGas({'from': univ_address}) #Calcula o gas estimado para executar a função
print('Preço do gas: {}'.format(gas_price))
print('Gas estimado: {}'.format(diploma_gas))
gas_fee = diploma_gas * gas_price #Valor da transação em wei
value_diploma = w3.fromWei(gas_fee, 'ether') #Valor da transação em ether
print('Custo da transação estimado: {}'.format(value_diploma))

def pagarTaxa():
    transfer = contract.functions.transferEther()
    transfer_gas = 40000
    transfer_txn = transfer.buildTransaction({
        'gas': transfer_gas,
        'value': gas_fee,
        'gasPrice': gas_price,
        'nonce': w3.eth.getTransactionCount(address_aluno)
    })
    signed_txn = w3.eth.account.signTransaction(transfer_txn, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print(receipt)


def registrarDiploma(discente, dataNascimento, curso, conclusao, cidade, iesEmissora, rgDiscente):
    diploma_txn = diploma.buildTransaction({
        'gas': diploma_gas,  # O gas estimado para realizar a transação
        'gasPrice': gas_price,
        'nonce': w3.eth.getTransactionCount(univ_address)
    })
    signed_txn2 = w3.eth.account.signTransaction(diploma_txn, private_key=private_key_univ)
    tx2_hash = w3.eth.sendRawTransaction(signed_txn2.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx2_hash)
    print(receipt)

op = -1
while(op != 0):
    print('=+=+=+=+=+= Menu =+=+=+=+=+=')
    print('1 - Pagar taxa')
    print('2 - Registrar diploma')
    print('0 - Sair')
    op = int(input('Escolha a opção: '))
    print('=+=+=+=+=+= Menu =+=+=+=+=+=')
    if op == 1:
        pagarTaxa()
    elif op == 2:
        registrarDiploma(discente, dataNasc, curso, conclusao, cidade, iesEmissora, rgDiscente)
    