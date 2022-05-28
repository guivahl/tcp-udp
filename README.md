# Lower case to upper case converter (UDP socket)

Course: Computer Networks <br>
Prof. Guilherme Correa <br>
Federal University of Pelotas (UFPEL) <br>
May 2022 <br>
Example of UDP application <br>
Requirements: Python3


Os códigos correspondem a uma aplicação cliente/servidor que utiliza o protocolo de transporte UDP para transferência de mensagens. A aplicação tem a seguinte função: o usuário digita uma frase em caixa baixa na aplicação cliente, que envia uma requisição ao servidor. O servidor, ao receber a frase em caixa baixa, faz a sua conversão para caixa alta (com o método upper) e envia a frase modificada ao cliente.

Seguem as tarefas que devem ser realizadas com base nos códigos disponibilizados:

1) Execute os dois códigos, de preferência em computadores separados, na sua rede local doméstica ou em uma rede virtual. Você pode usar dois computadores físicos ou duas máquinas virtuais e o software <a href="https://www.vpn.net/">Hamachi</a> para simular uma rede local. Algumas alterações poderão ser necessárias (por exemplo, substituir o 'hostname' pelo endereço IP do computador que vai rodar o código de servidor e o número de porta por um número de sua escolha, pré-combinado entre cliente e servidor).

2) Depois de testar com UDP, faça modificações no código para que a aplicação funcione com o protocolo TCP.

3) Com base nesta aplicação, crie uma nova aplicação que realize a conversão de caixa baixa para caixa alta e vice-versa. Para isso, crie um protocolo simples para indicar o tipo de mensagem que o cliente envia ao servidor (por exemplo, "CA <texto>" é uma mensagem do tipo caixa alta que deve ser convertida para caixa baixa no servidor, e "CB <texto>" é uma mensagem do tipo caixa baixa que deve ser convertida para caixa alta). O servidor deve ser capaz de identificar o tipo de mensagem, realizar a operação correta  e responder o texto convertido. Esta aplicação deve usar TCP como protocolo de transporte.
