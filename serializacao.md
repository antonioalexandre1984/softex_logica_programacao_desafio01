Suponha que temos uma classe chamada Cliente que possui os atributos nome, idade e endereço. Queremos serializar um objeto da classe Cliente para um arquivo no disco, e depois desserializar esse objeto a partir desse arquivo.

Para fazer isso, primeiro precisamos que a classe Cliente implemente a interface Serializable, que é uma marcação que indica que a classe pode ser serializada. O código da classe Cliente ficaria assim:

import java.io.Serializable;

public class Cliente implements Serializable {

    private String nome;
    private int idade;
    private String endereco;

    public Cliente(String nome, int idade, String endereco) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

}


Agora podemos criar um objeto da classe Cliente, serializá-lo para um arquivo no disco e depois desserializá-lo a partir desse arquivo. O código ficaria assim:

import java.io.*;

public class ExemploSerializacao {

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        
        Cliente cliente = new Cliente("João da Silva", 35, "Rua Fictícia, 123");
        
        // Serializar objeto para arquivo
        ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream("cliente.ser"));
        outputStream.writeObject(cliente);
        outputStream.close();
        
        // Desserializar objeto a partir do arquivo
        ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream("cliente.ser"));
        Cliente clienteDesserializado = (Cliente) inputStream.readObject();
        inputStream.close();
        
        // Imprimir informações do objeto desserializado
        System.out.println("Nome: " + clienteDesserializado.getNome());
        System.out.println("Idade: " + clienteDesserializado.getIdade());
        System.out.println("Endereço: " + clienteDesserializado.getEndereco());
        
    }

}
