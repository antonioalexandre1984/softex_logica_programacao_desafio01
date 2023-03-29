Creational Patterns: Factory Method Pattern
O padrão Factory Method é utilizado quando queremos criar um objeto, mas não sabemos exatamente qual classe deve ser utilizada na criação do objeto. O Factory Method é responsável por encapsular a criação do objeto em uma classe separada, que é responsável por retornar a instância apropriada do objeto com base em parâmetros fornecidos.

O padrão Factory Method geralmente envolve uma classe abstrata que define a interface para a criação de objetos e uma ou mais classes concretas que implementam essa interface e retornam a instância apropriada do objeto. O padrão é muito útil em situações em que precisamos lidar com objetos complexos ou em situações em que precisamos esconder os detalhes de criação de objetos do usuário final.

Structural Patterns: Adapter Pattern
O padrão Adapter é utilizado quando queremos adaptar uma interface existente para uma nova interface que possa ser usada por outras classes. O padrão Adapter permite que duas interfaces incompatíveis possam trabalhar juntas por meio de um adaptador.

O padrão Adapter é geralmente implementado por meio de uma classe que atua como intermediário entre duas classes incompatíveis. A classe adapta a interface de uma classe para a interface de outra classe para que possam trabalhar juntas de forma transparente.

O padrão Adapter é muito útil em situações em que precisamos reutilizar código existente que não pode ser modificado ou quando estamos trabalhando com classes de terceiros que possuem uma interface incompatível.

Behavioural Patterns: Observer Pattern
O padrão Observer é utilizado quando queremos notificar outras classes quando um objeto muda de estado. O padrão Observer é implementado por meio de uma classe observável e uma ou mais classes observadoras.

A classe observável é responsável por manter o estado do objeto e notificar todas as classes observadoras quando esse estado muda. As classes observadoras se registram na classe observável e recebem notificações quando o estado do objeto muda.

O padrão Observer é muito útil em situações em que precisamos notificar várias classes quando um objeto muda de estado, como em aplicações de tempo real ou em aplicações de interface do usuário em que o estado do objeto pode mudar com frequência.