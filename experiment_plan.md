# Plano de Experimentos RAG

Este documento prepara a documentação de teste para você executar e inserir os resultados.
Não altera o código, apenas define os parâmetros e as perguntas de comparação.

Utilize as seguintes perguntas para validar:
Perguntas de comparação

### Qual é o tema principal dos documentos?
- Quais são os personagens, entidades ou tópicos mais citados?
- Quais problemas de comunicação aparecem no texto?
- Há sinais de afastamento emocional no conteúdo?
- Resuma o conteúdo em até 3 frases curtas.

## Objetivo

Comparar o comportamento do sistema RAG em relação a:
- tamanho dos segmentos (chunks)
- número de documentos recuperados (top-k)
- uso de sobreposição entre segmentos
- temperatura do modelo
- qualidade das respostas em perguntas-chave

## Configuração base para todos os testes

Para cada experimento, mantenha todos os parâmetros fixos, exceto o que está sendo testado.

Configuração padrão recomendada:
- `chunk_size = 512 ou 256`
- `overlap = 80`
- `top_k = 4`
- `temperature = 0.3`
- `model_id = microsoft/Phi-3-mini-4k-instruct`

Por exemplo:
- No Experimento 1, altere somente `chunk_size` e deixe `overlap=80`, `top_k=4`, `temperature=0.3` e o modelo iguais.
- No Experimento 2, altere somente `top_k` e deixe `chunk_size=400`, `overlap=80`, `temperature=0.3` e o modelo iguais.
- No Experimento 3, altere somente `overlap` e deixe `chunk_size=400`, `top_k=4`, `temperature=0.3` e o modelo iguais.
- No Experimento 4, altere somente `temperature` e deixe `chunk_size=400`, `overlap=80`, `top_k=4` e o modelo iguais.
- No Experimento 5, altere somente o modelo e deixe `chunk_size=400`, `overlap=80`, `top_k=4`, `temperature=0.3` iguais.

## Experimentos sugeridos

### Experimento 1: Tamanho dos segmentos

Parâmetros:
- `chunk_size=300`, `overlap=80`
- `chunk_size=400`, `overlap=80`
- `chunk_size=500`, `overlap=80`

O que medir:
- clareza e precisão da resposta
- se o modelo usa mais ou menos contexto
- se respostas longas são mais completas ou mais erradas

# chunk_size = 300
## Para a pergunta: 1. Qual é o tema principal dos documentos?
 - obteve-se a seguinte resposta:
    -- RESPOSTA:
        Tema Principal: Comunicação deficitária entre duas pessoas próximas com sentimentos afetivos expressos.

        CHUNKS RECUPERADOS:

        [CHUNK 1]       
        14/02/2026 Olá, oli Devemos nos ter visto por pouco tempo. Infelizmente isso está sendo mais recorrente –       não sei se você nota isso... tampouco sei se você se importa. Melhorarei então, certo? Ser mais falante sobre tudo o que acontece. E peço perdão por ter falhado nisso. Como você acha que podemos

        [CHUNK 2]
        mim. E eu te amo muito. Oli, está tudo bem. E como assim eu devo mais claro? Não fui claro o bastante? Como você acha que podemos melhorar a comunicação? E o que você acha dessa situação toda? Gostaria de saber seu ponto de vista sobre isso ;-; Nos ver hoje daria certo – e deu. Mas foi uma espera não

        [CHUNK 3]
        por ora, como não pensar nisso. Muitas coisas ainda estão me preocupando, principalmente nós dois. Todo o medo e insegurança. Não sei se foi livramento... Salvo engano, não te contei os detalhes por estarmos de cricri. Mais uma vez, peço desculpas. Não me recordo de você ter me perguntado sobre se eu

        [CHUNK 4]
        sentes? Esse tratamento de indiferença está machucando. E, sinceramente, me pergunto todos os dias o motivo pelo qual você faz isso – lá no fundo eu sinto que já sei a resposta. Também não sei quais são os limites que você está estabelecendo. Mas sei – pois sinto – que o problema sou eu. Não queres
## Para a pergunta: 2. quais são os personagens, entidades ou tópicos mais citados?

        RESPOSTA:
        Personagem/Entidade Citado(s): "eu", "te" (referências à segunda parte da dupla), "outro".
        Tópico Cítado(s) Mínimo(s)/Máximo(s): Comunicação inadequada; necessidade de troca significativa de ideias e sentimento recíprocos nas interações sociais.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você espera, porque isso nunca existiu entre a gente, e você não perceber isso não me choca. Sempre estamos agindo conforme uma senoide, desde

        [CHUNK 2]
        com alguém. A vida é muito mais interessante quando a divido contigo – e quando há, nessa partilha, a reciprocidade. Uma outra dúvida: quando se relacionas comigo, se relacionas de verdade? Por mais que algumas questões resolva, eu, na terapia, eu sempre terei de me comunicar contigo. Comunicação é

        [CHUNK 3]
        não quero te perder, tampouco me afastar. Há outra saída. O que podemos mais fazer para que nós dois melhorarmos? Bom, tendo em vista que o problema sou eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação

        [CHUNK 4]
        ​ Primeiro que não existem regras para uma dinâmica de melhores amigos. Outra coisa, cada caso é um caso, e você não deveria analisar as coisas como sendo sempre uma comparação de quem é melhor ou o que for. Mais uma vez, não existem regras e como deve ser, nem todos os dias vai ser do mesmo jeito e
# chunk_size = 500
## Para a pergunta: 1. Qual é o tema principal dos documentos?
    
        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas de comunicação incluem falta de compreensão sobre papéis próprio versus alheio nas interações românticas, dificuldade em estabelecer limites claros sem pressupostos negativos, insatisfação com padrões esperados pela parceira diferentemente acordados pelo autor originalmente, incapacidade expressar necessidades específicas devido aos sentimentos subjacentes de abandono perceptivo, busca constante pelas respostas positivas afetivas ap

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        não quero e nem sou o centro do seu mundo. Você tem que começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo,

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 3]
        e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação é a chave de alguma relação sempre me referi a namoro, casamento. Uma comunicação de amizade não chega nem a 10% de uma comunicação de namoro. E caso você ainda não tenha percebido, a gente sempre está conversando e nunca chegando a algum lugar. Isso que eu acho deveras interessante é desgastante. Não tem porque eu sentir

        [CHUNK 4]
        nós. Infelizmente notei essa impressão de desinteresse, mas, de verdade, está tudo bem. A forma como me procuraste na quinta não foi uma das melhores. Meio que só seguisse com tua vida e, caso me visse, faria uma intervenção. Não senti que você realmente queria me ver. Deverias ter sido, você, mais clara. Muito mais. Nós dois temos que melhorar a comunicação. Está ficando muito difícil. E, infelizmente, está sendo um pouco difícil para a fazer o Entendi. Pensei que você tivesse chamado ele e só
        Digite sua pergunta: 

## chuck_size = 512

        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas identificados incluem falta de confiança entre os parceiros (você quer estar constantemente à frente), comparação inútil com outras pessoas, dificuldade em manter distância emocional/comunicação ("ele" parece menos importante) e insatisfação generalizada devido a "falhas constantes". Há também indiretamente mencionadas questões sobre interferências nas vidas dos participantes sem buscar resolução adequada ('desentendimentos', 'd

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        não quero e nem sou o centro do seu mundo. Você tem que começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo,

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 3]
        e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação é a chave de alguma relação sempre me referi a namoro, casamento. Uma comunicação de amizade não chega nem a 10% de uma comunicação de namoro. E caso você ainda não tenha percebido, a gente sempre está conversando e nunca chegando a algum lugar. Isso que eu acho deveras interessante é desgastante. Não tem porque eu sentir

        [CHUNK 4]
        nós. Infelizmente notei essa impressão de desinteresse, mas, de verdade, está tudo bem. A forma como me procuraste na quinta não foi uma das melhores. Meio que só seguisse com tua vida e, caso me visse, faria uma intervenção. Não senti que você realmente queria me ver. Deverias ter sido, você, mais clara. Muito mais. Nós dois temos que melhorar a comunicação. Está ficando muito difícil. E, infelizmente, está sendo um pouco difícil para a fazer o Entendi. Pensei que você tivesse chamado ele e só
        Digite sua pergunta:

        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas identificados incluem falta de confiança entre os parceiros (você quer estar constantemente à frente), comparação inútil com outras pessoas, dificuldade em manter distância emocional/comunicação ("ele" parece menos importante) e insatisfação generalizada devido a "falhas constantes". Há também indiretamente mencionadas questões sobre interferências nas vidas dos participantes sem buscar resolução adequada ('desentendimentos', 'd

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        não quero e nem sou o centro do seu mundo. Você tem que começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo,

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 3]
        e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação é a chave de alguma relação sempre me referi a namoro, casamento. Uma comunicação de amizade não chega nem a 10% de uma comunicação de namoro. E caso você ainda não tenha percebido, a gente sempre está conversando e nunca chegando a algum lugar. Isso que eu acho deveras interessante é desgastante. Não tem porque eu sentir

        [CHUNK 4]
        nós. Infelizmente notei essa impressão de desinteresse, mas, de verdade, está tudo bem. A forma como me procuraste na quinta não foi uma das melhores. Meio que só seguisse com tua vida e, caso me visse, faria uma intervenção. Não senti que você realmente queria me ver. Deverias ter sido, você, mais clara. Muito mais. Nós dois temos que melhorar a comunicação. Está ficando muito difícil. E, infelizmente, está sendo um pouco difícil para a fazer o Entendi. Pensei que você tivesse chamado ele e só

        Digite sua pergunta: há sinais de afastamento emocional no conteúdo?

        RESPOSTA:
        Sim, há indícios de distanciamento emocional ao longo dos trechos discutidos; expressões indicam falta de interesse genuíno nas conversas e dificuldade em manter relacionamentos próximos. Houve também referências à necessidade de melhora na comunicação entre os participantes. No entanto, sem detalhes adicionais específicos, esta análise baseia-se exclusivamente nos fragmentos apresentados. Se considerarmos todo o material disponível, seria importante buscar confirmar ainda

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 3]
        nós. Infelizmente notei essa impressão de desinteresse, mas, de verdade, está tudo bem. A forma como me procuraste na quinta não foi uma das melhores. Meio que só seguisse com tua vida e, caso me visse, faria uma intervenção. Não senti que você realmente queria me ver. Deverias ter sido, você, mais clara. Muito mais. Nós dois temos que melhorar a comunicação. Está ficando muito difícil. E, infelizmente, está sendo um pouco difícil para a fazer o Entendi. Pensei que você tivesse chamado ele e só

        [CHUNK 4]
        me disse que ficou “magoado”? Já disse para continuar da mesma forma. Rapaz, o cricri aqui acontece 80% das vezes do nosso tempo, eu diria, pode até ser menos. Você sabe como eu ajo se as coisas estão normais, mas nem sempre que estão normais eu vou agir que nem o dia da prova de quinta feira, porque não existe um padrão. Mas é exatamente assim como você age quando você se compara, apesar de ter o medo de ser trocado. O seu final, não condiz com nada do que falei nesse parágrafo. Não é que antes
        Digite sua pergunta: quais são os personangens, entidades ou tópicos mais citados?

        RESPOSTA:
        Os principais assuntos mencionados incluem "reciprocidade", "melhores amigos" (comentários feitos anteriormente), questões de autoestima ("eu nunca vou aceitar estar num segundo plano"), importância da comunicação dentro das relações ("A comunicação é a chave...") e desafios associados aos laços íntimos ("falta de proximidade"). Não foi identificado explicitamente nomes individuais ou outras entidades relevantes nestes segmentos selecionados.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        [...] 28 de março de 2026 Olá. Oli. Espero que estejas bem! De fato, não existem regras para melhores amigos. Entretanto, existe uma certa dinâmica, um certo padrão. Uma certa – como já havia falado – reciprocidade. Sei bem que cada caso é um caso, mas os padrões, no nosso caso, não existem. Sei que nem todos os dias serão iguais, mas, nos casos de melhores amigos, há uma certa essência e um certo padrão – já comentei, em RB_22, o que acho sobre ser melhores amigos. Muitas perguntas minhas não foram

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 3]
        não quero e nem sou o centro do seu mundo. Você tem que começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo,

        [CHUNK 4]
        que, antigamente, eu não via, para mim, sentido em ir à terapia? Por isso não fazia. Estou tentando, de verdade, melhorar. Muitas coisas ainda são confusas para mim e entro direto em conflitos. E, às vezes, não dá para esperar até a próxima sessão para tentar encontrar uma luz em meio a tanta escuridão. A vida é mais legal quando compartilhada com alguém. A vida é muito mais interessante quando a divido contigo – e quando há, nessa partilha, a reciprocidade. Uma outra dúvida: quando se relacionas

### Experimento 2: Número de segmentos recuperados (`top_k`)

Parâmetros:
- `top_k=2`
- `top_k=4`
- `top_k=6`

O que medir:
- se mais contexto melhora a resposta
- se respostas com `top_k=6` ficam redundantes ou inconsistentes
- se respostas com `top_k=2` perdem informação

## top_k = 2
        Digite sua pergunta: há sinais de afastamento emocional no conteúdo?

        RESPOSTA:
        Sim, há indícios de desconforto emocional relacionados à busca pela atenção constante e ao sentimento incompreensível expressado pelo interlocutor quanto aos problemas dos outros nas relações amorosas.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 2]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        Digite sua pergunta: quais são os personagens, entidades ou tópicos mais citados?

        RESPOSTA:
        Os principais personagens mencionados incluem "você" (referindo-se ao falante) e alguém cujas dificuldades ele/ela discute; também está presente 'outra pessoa', indicativo de comparação entre diferentes individuios dentro dessa dinâmica relacional. O tema central abordado refere-se às questões sobre autossuficiência emocional e importância da independência individual versus dependencia excessiva numa parceria romântica. A necessidade de trabal

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        normal do cotidiano com alguma pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho

        [CHUNK 2]
        não quero e nem sou o centro do seu mundo. Você tem que começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo,
        Digite sua pergunta: 


## top_k = 6

        Digite sua pergunta: há sinais de afastamento emocional no conteúdo?

        RESPOSTA:
        Há indícios claros de distância emocional nas expressões "me compare", "sem certeza" e "falhar". Essas palavras indicam sentimentos internos negativos relacionados aos conflitos interpessoais apresentados. Além disso, declarações como "nenhum prazer neles," mostram insatisfação profunda quanto à dinâmica dos laços familiares presentes durante festas passadas. Isso reforça a ideia de tensão subjacente dentro dessas relações

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 2]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 3]
        precisamos disse de volta. Precisamos entrar, novamente, em sintonia. Numa frequência boa para os dois. Na teoria tudo funcionaria perfeitamente. Porém, na prática, isso não ocorre. Mesmo que eu lute bastante, nunca é o suficiente. Não acho/sinto que arrumei conforto nesse desconforto todo. A terapia, assim como o psiquiatra são ações novas, ainda, para mim. E lembra-te que, antigamente, eu não via, para mim, sentido em ir à terapia? Por isso não fazia. Estou tentando, de verdade, melhorar. Muitas coisas ainda

        [CHUNK 4]
        que ficou “magoado”? Já disse para continuar da mesma forma. Rapaz, o cricri aqui acontece 80% das vezes do nosso tempo, eu diria, pode até ser menos. Você sabe como eu ajo se as coisas estão normais, mas nem sempre que estão normais eu vou agir que nem o dia da prova de quinta feira, porque não existe um padrão. Mas é exatamente assim como você age quando você se compara, apesar de ter o medo de ser trocado. O seu final, não condiz com nada do que falei nesse parágrafo. Não é que antes havia sintonia, antes

        [CHUNK 5]
        não está entregando troféus. Me comparo – uma idiotice, sei bem –, pois quando vejo você e alguma outra pessoa, sinto muitas coisas – que você já está cansada de saber. Não me comparo porque quero, mas para entender o motivo que para fulano é uma coisa e para mim, outra. Às vezes é muito difícil te entender. Sim, sei muito bem que já comentaste sobre. A mencionei porque precisamos disse de volta. Precisamos entrar, novamente, em sintonia. Numa frequência boa para os dois. Na teoria tudo funcionaria perfeitamente.

        [CHUNK 6]
        trivial. Por mais que eu tente, haverá um momento de falha. E, nesse momento, lascou-se tudo. Não era somente por isso. Mas eu sempre recomendava que meus colegas fossem ao psicólogo. Eu não via sentido para mim. Sendo bem sincero, já me falaram que eu não tinha mais jeito. E, dado tudo o que ocorre, acho que estão certos. Oli, “reluto” para ir ao psiquiatra, como bem sabes, pelo medo da piora. Conheço algumas pessoas que pioraram com algum medicamento. Reluto para ir pois não confio tanto no SUS. Reluto para
        Digite sua pergunta: quais são os personagens, entidades ou tópicos mais citados?

        RESPOSTA:
        Os principais personagens mencionados incluem 'você', referenciando alguém específico (possivelmente um membro próximo) cujos comportamentos causaram preocupação recorrentes. Outros elementos destacados são 'minha família,' representando parentes íntimos participantes anteriormente felizes juntos, e 'ele/ela [Entendido],' possivelmente designando um mediador externo involucrado recentemente na situação discutida. As questões centrais giram em torno da d

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você espera, porque isso nunca existiu entre a gente, e você não perceber isso não me choca. Sempre estamos agindo conforme uma senoide, desde sempre. O ponto é que antes você só não era tão paranóico sobre a nossa amizade e eu realmente não sei em que momento ou o que fez isso mudar. Eu acho que arrumou, por mais que você fale que tente, você continua repetindo os mesmos padrões. Você não via sentido

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        mundo, mas é uma parte importante dele. Isso incomoda-te muito? A vida é legal ao lado dos meus amigos, mas a vida é mais legal ao lado da miguxa. Desculpa por isso. Mas, se for do seu desejo, não vai mais ocorrer. E eu sei que não está saudável isso. Mas, ressalto, não quero te perder, tampouco me afastar. Há outra saída. O que podemos mais fazer para que nós dois melhorarmos? Bom, tendo em vista que o problema sou eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações.

        [CHUNK 4]
        [...] 28 de março de 2026 Olá. Oli. Espero que estejas bem! De fato, não existem regras para melhores amigos. Entretanto, existe uma certa dinâmica, um certo padrão. Uma certa – como já havia falado – reciprocidade. Sei bem que cada caso é um caso, mas os padrões, no nosso caso, não existem. Sei que nem todos os dias serão iguais, mas, nos casos de melhores amigos, há uma certa essência e um certo padrão – já comentei, em RB_22, o que acho sobre ser melhores amigos. Muitas perguntas minhas não foram respondidas

        [CHUNK 5]
        verdade, está tudo bem. A forma como me procuraste na quinta não foi uma das melhores. Meio que só seguisse com tua vida e, caso me visse, faria uma intervenção. Não senti que você realmente queria me ver. Deverias ter sido, você, mais clara. Muito mais. Nós dois temos que melhorar a comunicação. Está ficando muito difícil. E, infelizmente, está sendo um pouco difícil para a fazer o Entendi. Pensei que você tivesse chamado ele e só depois que foi falar comigo;-; Não é legal sofrer em silêncio. E não precisa

        [CHUNK 6]
        começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação
        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas identificados de comunicação incluem falta de compreensão mutua ("nunca va...") e incapacidade de manter conexões significativas sem culpar ('porco'). Existe também desconforto relativo ao papel do destinatário sendo constantemente focalizado pelos outros ('ser o centro'), levantando questionamentos sobre expectativa versus capacidade individual de compartilhamento genuíno. Finalmente, surgem obstáculos percebidos tanto pela parte originadora quanto recebedora devido às diferen

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 4]
        que será deste nosso laço? O que achas disso tudo? O que tu sentes? Esse tratamento de indiferença está machucando. E, sinceramente, me pergunto todos os dias o motivo pelo qual você faz isso – lá no fundo eu sinto que já sei a resposta. Também não sei quais são os limites que você está estabelecendo. Mas sei – pois sinto – que o problema sou eu. Não queres mais fazer e/ou falar comigo.

        [CHUNK 5]
        esse. Também queria que fosse assim. E eu sei que o problema sou eu. Se, por acaso, eu não existisse, nada disso estaria acontecendo. Não é sobre nos vermos para ficar no mesmo enredo, Oli. Não é que eu sempre vou querer ser o “centro” das atenções. Não é sobre isso. Não mais falarei, contigo, sobre esse assunto de amizades. Trate-me como bem quiser e quando quiser. Eu devo, somente, aceitar, né isso? Antes havia uma sintonia. Se quiseres explicar e contextualizar o motivo pelo quando nunca estivemos em sintonia,

        [CHUNK 6]
        – e quando há, nessa partilha, a reciprocidade. Uma outra dúvida: quando se relacionas comigo, se relacionas de verdade? Por mais que algumas questões resolva, eu, na terapia, eu sempre terei de me comunicar contigo. Comunicação é chave de qualquer relação – você já me disse sobre. E uma relação é entre duas pessoas. E precisa-se de conversa para que haja resolução. Descanse. Ficarei esperando as respostas, os comentários.... Ficarei esperando a ti. Sentes minha falta? Se você não sabe, quem é que sabe? Por
        Digite sua pergunta: 


### Experimento 3: Sobreposição entre segmentos

Parâmetros:
- `overlap=0`
- `overlap=80`

## overlap=0

        Digite sua pergunta: quais problemas de comunicaçao aparecem no texto?

        RESPOSTA:
        Os principais problemas identificados incluem dependencia excessiva nas interações dos amigos (problemática), comparação constante com outras pessoas sem reconhecer suas próprias necessidades individuais (falta de autoestima) e desconexão entre palavras faladas e pensamentos internos (discrepância). Além disso, existem preocupações quanto à incapacidade do narrador de manter relacionamentos equilibrados devido aos seus comportamentos centraisistas ("ser o centro" das at

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 4]
        que será deste nosso laço? O que achas disso tudo? O que tu sentes? Esse tratamento de indiferença está machucando. E, sinceramente, me pergunto todos os dias o motivo pelo qual você faz isso – lá no fundo eu sinto que já sei a resposta. Também não sei quais são os limites que você está estabelecendo. Mas sei – pois sinto – que o problema sou eu. Não queres mais fazer e/ou falar comigo.
        Digite sua pergunta: quais são os personagens, entidades ou tópicos mais citados?

        RESPOSTA:
        Personagem principal - Narrador; Amigo(s); Migaxias/Miguxas; Terapeuta.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você espera, porque isso nunca existiu entre a gente, e você não perceber isso não me choca. Sempre estamos agindo conforme uma senoide, desde sempre. O ponto é que antes você só não era tão paranóico sobre a nossa amizade e eu realmente não sei em que momento ou o que fez isso mudar. Eu acho que arrumou, por mais que você fale que tente, você continua repetindo os mesmos padrões. Você não via sentido

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        mundo, mas é uma parte importante dele. Isso incomoda-te muito? A vida é legal ao lado dos meus amigos, mas a vida é mais legal ao lado da miguxa. Desculpa por isso. Mas, se for do seu desejo, não vai mais ocorrer. E eu sei que não está saudável isso. Mas, ressalto, não quero te perder, tampouco me afastar. Há outra saída. O que podemos mais fazer para que nós dois melhorarmos? Bom, tendo em vista que o problema sou eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações.

        [CHUNK 4]
        [...] 28 de março de 2026 Olá. Oli. Espero que estejas bem! De fato, não existem regras para melhores amigos. Entretanto, existe uma certa dinâmica, um certo padrão. Uma certa – como já havia falado – reciprocidade. Sei bem que cada caso é um caso, mas os padrões, no nosso caso, não existem. Sei que nem todos os dias serão iguais, mas, nos casos de melhores amigos, há uma certa essência e um certo padrão – já comentei, em RB_22, o que acho sobre ser melhores amigos. Muitas perguntas minhas não foram respondidas
        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas de Comunicação Identificados No Texto: Dependência Excessiva Nas Interações Com Amigos, Falta De AutoEstima Devido À Comparação Constante Sem Reconhecimento Dos Seus Própcios Pensamentos Individuais, Discrepâncias Entre Palavras Faladas E Crenças Internas Do Sujeito Que Estuda Como Um Centro Das Atenções Em Relacionamentos.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 4]
        que será deste nosso laço? O que achas disso tudo? O que tu sentes? Esse tratamento de indiferença está machucando. E, sinceramente, me pergunto todos os dias o motivo pelo qual você faz isso – lá no fundo eu sinto que já sei a resposta. Também não sei quais são os limites que você está estabelecendo. Mas sei – pois sinto – que o problema sou eu. Não queres mais fazer e/ou falar comigo.
        Digite sua pergunta: 

O que medir:
- se a sobreposição melhora a continuidade do contexto
- se a sobreposição introduz repetição demais
- se sem overlap a recuperação perde partes importantes

### Experimento 4: Temperatura do modelo

Parâmetros:
- `temperature=0.0`
- `temperature=0.3`
- `temperature=0.7`

## temp = 0.1 -- 0.0 não funcionou; tem que colocar o do_sample = False

        Digite sua pergunta: há sinais de afastamento emocional no conteúdo?

        RESPOSTA:
        Sim, existem indícios de distância emocional ao longo dos trechos discutidos; ambos expressam sentimentos negativos relacionados aos conflitos interpessoais sem buscar resolução clara.

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 2]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 3]
        precisamos disse de volta. Precisamos entrar, novamente, em sintonia. Numa frequência boa para os dois. Na teoria tudo funcionaria perfeitamente. Porém, na prática, isso não ocorre. Mesmo que eu lute bastante, nunca é o suficiente. Não acho/sinto que arrumei conforto nesse desconforto todo. A terapia, assim como o psiquiatra são ações novas, ainda, para mim. E lembra-te que, antigamente, eu não via, para mim, sentido em ir à terapia? Por isso não fazia. Estou tentando, de verdade, melhorar. Muitas coisas ainda

        [CHUNK 4]
        que ficou “magoado”? Já disse para continuar da mesma forma. Rapaz, o cricri aqui acontece 80% das vezes do nosso tempo, eu diria, pode até ser menos. Você sabe como eu ajo se as coisas estão normais, mas nem sempre que estão normais eu vou agir que nem o dia da prova de quinta feira, porque não existe um padrão. Mas é exatamente assim como você age quando você se compara, apesar de ter o medo de ser trocado. O seu final, não condiz com nada do que falei nesse parágrafo. Não é que antes havia sintonia, antes
        Digite sua pergunta: quais são os personagens, entidades ou tópicos mais citados?

        RESPOSTA:
        Os principais personagens mencionados nas discussões incluem "você", referenciando alguém específico (possivelmente 'Rodrigo'), e também outros participantes ("meu namorado" - possível nome próprio), juntamente com elementos metafóricos representados pela figura da "migax". As questões centrais giram em torno da dificuldade encontrada pelos protagonistas em manter sua amizade devido às diferenças individuais e expectativas irreconciliá

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você espera, porque isso nunca existiu entre a gente, e você não perceber isso não me choca. Sempre estamos agindo conforme uma senoide, desde sempre. O ponto é que antes você só não era tão paranóico sobre a nossa amizade e eu realmente não sei em que momento ou o que fez isso mudar. Eu acho que arrumou, por mais que você fale que tente, você continua repetindo os mesmos padrões. Você não via sentido

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        mundo, mas é uma parte importante dele. Isso incomoda-te muito? A vida é legal ao lado dos meus amigos, mas a vida é mais legal ao lado da miguxa. Desculpa por isso. Mas, se for do seu desejo, não vai mais ocorrer. E eu sei que não está saudável isso. Mas, ressalto, não quero te perder, tampouco me afastar. Há outra saída. O que podemos mais fazer para que nós dois melhorarmos? Bom, tendo em vista que o problema sou eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações.

        [CHUNK 4]
        [...] 28 de março de 2026 Olá. Oli. Espero que estejas bem! De fato, não existem regras para melhores amigos. Entretanto, existe uma certa dinâmica, um certo padrão. Uma certa – como já havia falado – reciprocidade. Sei bem que cada caso é um caso, mas os padrões, no nosso caso, não existem. Sei que nem todos os dias serão iguais, mas, nos casos de melhores amigos, há uma certa essência e um certo padrão – já comentei, em RB_22, o que acho sobre ser melhores amigos. Muitas perguntas minhas não foram respondidas
        Digite sua pergunta: 

## temp = 0.9

        Digite sua pergunta: há sinais de afastamento emocional no conteúdo?

        RESPOSTA:
        Sim, existem indícios de tensão interpessoal nas expressões "Acertei", reconhecimento dos problemas sem resolução adequada e sentimentos misturados ao discutir relacionamentos íntimos ("nossa"), reflexões introspectivas indicando mal-estar interno (“junto”, “melhor estáva lá dentro”), alusão implícita aos confrontos recorrentes evidenciadas pelo termo ‘crick’ - referindo-se geralmente a discussões contundentes frequent

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 2]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 3]
        precisamos disse de volta. Precisamos entrar, novamente, em sintonia. Numa frequência boa para os dois. Na teoria tudo funcionaria perfeitamente. Porém, na prática, isso não ocorre. Mesmo que eu lute bastante, nunca é o suficiente. Não acho/sinto que arrumei conforto nesse desconforto todo. A terapia, assim como o psiquiatra são ações novas, ainda, para mim. E lembra-te que, antigamente, eu não via, para mim, sentido em ir à terapia? Por isso não fazia. Estou tentando, de verdade, melhorar. Muitas coisas ainda

        [CHUNK 4]
        que ficou “magoado”? Já disse para continuar da mesma forma. Rapaz, o cricri aqui acontece 80% das vezes do nosso tempo, eu diria, pode até ser menos. Você sabe como eu ajo se as coisas estão normais, mas nem sempre que estão normais eu vou agir que nem o dia da prova de quinta feira, porque não existe um padrão. Mas é exatamente assim como você age quando você se compara, apesar de ter o medo de ser trocado. O seu final, não condiz com nada do que falei nesse parágrafo. Não é que antes havia sintonia, antes
        Digite sua pergunta: quais problemas de comunicação aparecem no texto?

        RESPOSTA:
        Problemas identificados incluem falta de compreensão mutua desde cedo; busca constante pela exclusividade do narrador; deficiências percebidas tanto quanto necessidades próprias durante reuniões significativas; ausência concreta de feedback positivo ou solucionista após distância física intensificada pelas diferenças ideológicas originais; desconforto relativo à imprecisão de palavras utilizadas anteriormente apontadas devido às consequências pragmáticas incomuns decor

        CHUNKS RECUPERADOS:

        [CHUNK 1]
        começar a se entender melhor e separar muito bem isso, você tem vários amigos, e se a vida não fosse interessante ao lado deles, você não passaria o dia com eles. Você realmente tem que aprender a lidar na terapia com essa dependência e demandar energia para outros locais. Porque nem de longe isso é uma amizade saudável. Eu sempre disse e digo que comunicação é a chave de qualquer relação, mas essa comunicação aqui que a gente tem faz tempo, nunca vai ser a chave dessa amizade. E quando eu me refiro a comunicação

        [CHUNK 2]
        pessoa, não algo que sempre tem um problema, um “e se”. Você se comparar com outra pessoa da minha vida é a coisa mais ridícula que existe, e você deveria tratar na terapia o porquê você sempre vai querer ser o “centro” das atenções na vida de quem ama. E porque não sabe separar as coisas. É bom você tentar chegar em algum lugar nisso, porque como já bem pontuei eu não suporto mais ouvir esse tópico, porque realmente, não cabe a mim te explicar nada disso. Eu acho muito difícil entrarmos em sintonia como você

        [CHUNK 3]
        eu, tenho de me ajeitar. Acho que seja isso. Para mim, a conversa é a base de todas as relações. Claro que há situações que pedem mais comunicação e outras que pedem menos. Acredito que o que possa faltar na gente é uma certa coerência entre o que é dito e o que é falado. Talvez possa ser isso. Talvez possa ser outra coisa. Não sei. Mas, como você já disse – e eu sei – , o problema sou eu. A situação na qual nos encontramos ontem não foi uma boa situação. E não a aproveitamos, foi, somente, sobre cricri. Enfim.

        [CHUNK 4]
        que será deste nosso laço? O que achas disso tudo? O que tu sentes? Esse tratamento de indiferença está machucando. E, sinceramente, me pergunto todos os dias o motivo pelo qual você faz isso – lá no fundo eu sinto que já sei a resposta. Também não sei quais são os limites que você está estabelecendo. Mas sei – pois sinto – que o problema sou eu. Não queres mais fazer e/ou falar comigo.
        Digite sua pergunta:    

O que medir:
- consistência / fidelidade às informações
- se `0.0` produz texto mais preciso
- se `0.7` traz maior variação e possíveis alucinações

### Experimento 5: Comparação de modelos (se possível)

Parâmetros:
- modelo atual: `microsoft/Phi-3-mini-4k-instruct`
- outro modelo disponível na sua máquina ou via API

O que medir:
- qualidade das respostas
- velocidade de geração
- custo ou consumo de recursos

## Perguntas para comparar nos testes

Use as mesmas perguntas em todos os experimentos para comparar melhor.

1. Qual é o tema principal dos documentos?
2. Quais são os personagens, entidades ou tópicos mais citados?
3. Quais problemas de comunicação aparecem no texto?
4. Há sinais de afastamento emocional no conteúdo?
5. Resuma o conteúdo em até 3 frases curtas.

## Como documentar cada experimento

Para cada configuração, registre:
- configuração usada (`chunk_size`, `overlap`, `top_k`, `temperature`, modelo)
- pergunta aplicada
- resposta gerada pelo sistema
- observação sobre precisão, riqueza de informação e coerência
- nota final: melhor / aceitável / ruim

## Estrutura recomendada de resultados

1. Configuração escolhida
2. Perguntas aplicadas
3. Resposta do sistema
4. Observações de qualidade
5. Conclusão breve

## Notas importantes

- Use o mesmo conjunto de perguntas para comparar mudanças.
- Mantenha as respostas do mesmo experimento lado a lado para facilitar a análise.
- Em um slide, coloque pelo menos um exemplo com `top_k=4` e outro com `top_k=2`.
- Em outro slide, compare `overlap=0` com `overlap=80`.
