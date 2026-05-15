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
- `chunk_size = 400`
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

### chuck_size = 512

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

### Experimento 2: Número de segmentos recuperados (`top_k`)

Parâmetros:
- `top_k=2`
- `top_k=4`
- `top_k=6`

O que medir:
- se mais contexto melhora a resposta
- se respostas com `top_k=6` ficam redundantes ou inconsistentes
- se respostas com `top_k=2` perdem informação

### Experimento 3: Sobreposição entre segmentos

Parâmetros:
- `overlap=0`
- `overlap=80`

O que medir:
- se a sobreposição melhora a continuidade do contexto
- se a sobreposição introduz repetição demais
- se sem overlap a recuperação perde partes importantes

### Experimento 4: Temperatura do modelo

Parâmetros:
- `temperature=0.0`
- `temperature=0.3`
- `temperature=0.7`

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
