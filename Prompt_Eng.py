

'''
Prompting:

==================================================================================
Content;

Context-based Prompting                         Core Strategy
Specificity-based Prompting
==================================================================================
Direct Question Prompting
Instructional Prompting
Senario Based Prompting                         6 Style in Prompting
Conversational Prompting
Compartive Prompting
Fill in the Blanck 
==================================================================================
Write Clear and specific instruction            Pranciples in Prompting
Give the model time to think
==================================================================================
Iterative prompting
Summarizing
Inferring
Transforming
==================================================================================


    Core Strategie in prompting;
    
    When we want to have an interaction with a language model like ChatGPT, it is crucial to know how to 
    speak or chat with it effectively!

    There are different techniques in prompt engineering that help us guide the model’s responses and 
    improve the quality of its output. Two such techniques are:

    1. Context-Based Prompting
        In this technique, we define both the Task we want the language model to perform and the Context 
        in which the task is being done.
        Providing rich and clear context helps the model better understand the background and purpose of 
        the task, just like when we explain a topic in detail to another person so they can give informed
        feedback or perform an action appropriately.

    Structure:
        Task: What you want the model to do.

        Context: The background information, constraints, or related content that helps the model 
        understand your request better.

    Example:
        Task: Summarize the following article in three bullet points.
        Context: The article is about climate change, focusing on the rise in global temperatures over the
        last 50 years, the role of carbon emissions, and the actions taken by governments worldwide.

    2. Specificity-Based Prompting
        In this technique, the prompt should be precise and to the point, clearly telling the model 
        exactly what to do. This approach works best when you don’t need to provide background context and 
        the task can be completed with minimal ambiguity.

    Structure:
        Task: A clear and specific instruction.

    Example:
        Task: Translate the following sentence into Persian: "Knowledge is power."


    Both methods are useful depending on the situation:
    Use context-based prompting when the model needs more background to perform well.
    Use specificity-based prompting when the task is straightforward and doesn’t require explanation.
    
    ======================================================================================================

    Six Styles in Prompting
    
    There are six common prompting styles that we can use depending on the nature of our task and the 
    desired response from a language model. Each style has a specific structure and is suitable for 
    different use cases.

    1. Direct Question Prompts
    Structure: Ask a clear and specific question that requires a factual or informative answer.

    Example:
    Question: What are the main causes of climate change?

    This style is best used when you want concise and focused information.

    2. Instructional Prompts
    Structure: Give the model a direct command or instruction, often beginning with verbs like "Write,"
    "List," "Explain," "Describe", or "Generate".

    Example:
    Instruction: Write a short paragraph explaining how photosynthesis works.

    Use this when you want the model to perform a task in a specific format or tone.

    3. Scenario-Based Prompts
    Structure: Describe a situation or scenario, then ask the model to respond or act accordingly.

    Example:
    Prompt: Imagine you are a teacher explaining Newton's laws to a group of 12-year-old students. How 
    would you explain the first law?

    This is effective for role-playing, simulations, or testing creative and situational understanding.

    4. Conversational Prompts
    Structure: Set up a back-and-forth dialogue or start a conversation where the model continues 
    naturally.

    Example:
    Prompt:
    User: Hi, can you help me plan a trip to Iran?
    Assistant: Of course! When are you planning to go and what kind of experiences are you looking for?

    This is great for simulating realistic dialogue or chatbot interactions.

    5. Comparative Prompts
    Structure: Ask the model to compare two or more items, concepts, or approaches.

    Example:
    Prompt: Compare Python and JavaScript in terms of ease of learning, performance, and typical use 
    cases.

    Use this style for analytical or decision-making support.

    6. Fill-in-the-Blank Prompts
    Structure: Present a sentence or paragraph with missing information and ask the model to complete it.

    Example:
    Prompt: Artificial intelligence is transforming the world by __________.

    This is useful for creativity, testing comprehension, or language exercises.

    ====================================================================================================

    Prompting Principles
        In prompting there are some principle that we have to commit to them to get a effective results.
        The principles are;
            Principle 1: Write clear and specific instructions
            Principle 2: Give the model time to “think”

        Baised on these two principle we will have different tactis in prompting with an LM models.

        For Principle 1, we will have 4 tactics that we can see them in the following;

        Tactic 1: "Use delimiters" to clearly indicate distinct parts of the input.
                  Delimiters can be anything like: ```, < >, `<tag> </tag>`, `:`, """
                  It is crucial HOW WE INJECT INPUT TO MODEL. So, in RAG based models changing input
                  documents in understandable form for models should be considered.
                  For example, Here a sutibale formed input text for injecting to model has been writtin
                  text = f """
                            You should express what you want a model to do by \ 
                            providing instructions that are as clear and \ 
                            specific as you can possibly make them. \ 
                            This will guide the model towards the desired output, \ 
                            and reduce the chances of receiving irrelevant \ 
                            or incorrect responses. Don't confuse writing a \ 
                            clear prompt with writing a short prompt. \ 
                            In many cases, longer prompts provide more clarity \ 
                            and context for the model, which can lead to \ 
                            more detailed and relevant outputs.
                          """
                 As you can see each line are saprated by "\" from each other. This delimiter indicate 
                 distincs of each line in text. So, It would understanabel for model in reading it.

                 Now, we should tell the model to know what should it does!
                 We should use these delimiter in our prompting. This tactic allows use to clearly tell
                 the model its task.
                 For instanse, Here a sutiable formed prompt has been writtin;
                 prompt = f """
                            Summarize the text delimited by triple backticks \ 
                            into a single sentence.
                            ```{text}```
                            """
                As you can see line sperate with "\" and in the text we specified the task and 
                where it should model be applied its duity by saying "triple backticks"

        Tactic 2: Ask for a structured output like instructioanl prompting.
                  In this tactic we will able to generate the output in other type of language programming.
                  like JSON and HTML
                  To do this, we can use Generate, Write, Describe, and Explain keywords as starter.
                  This tactic will be set in the specificity-based prompting method.
                  because we will inject just task we want to model apply on it.
                  For instanse;
                  prompt = f """
                                Generate a list of three made-up book titles along \ 
                                with their authors and genres. 
                                Provide them in JSON format with the following keys: 
                                book_id, title, author, genre.
                             """
                  As we can see, the commande is seprated by "\" and forced model to generate it in JSON
                  format.
        Tactic 3: Ask the model to check whether conditions are satisfied or the same Comparative prompting
                  or Conditional prompting.
                  In this tactic, we will be provided to model a command that is in conditional form.                  
                  prompt = f"""
                            You will be provided with text delimited by triple quotes. 
                            If it contains a sequence of instructions, \ 
                            re-write those instructions in the following format:

                            Step 1 - ...
                            Step 2 - …
                            …
                            Step N - …

                            If the text does not contain a sequence of instructions, \ 
                            then simply write \"No steps provided.\"

                            \"\"\"{text_1}\"\"\"
                            """
                  As we can see, this prompt has two part. the first is our first condition that told the 
                  model to do specific task and the other is our second condition that is opposit of the first
                  condition.
                  Beside all spcrips, we can see by using delimiters we can throw the prompt clearly to model.

        Tactic 4: "Few-shot" prompting or Scenario-based prompting.    
                  This Tactic will be placed in Context based prompting cluster because we say task and context.
                  prompt = f"""
                            Your task is to answer in a consistent style.

                            <child>: Teach me about patience.

                            <grandparent>: The river that carves the deepest \ 
                            valley flows from a modest spring; the \ 
                            grandest symphony originates from a single note; \ 
                            the most intricate tapestry begins with a solitary thread.

                            <child>: Teach me about resilience.
                            """  

        For Principle 2, we will have 2 tactics that we can see them in the following; 

        Tactic 1: Specify the steps required to complete a task.
                  For instance;
                  prompt_1 = f"""
                            Perform the following actions: 
                            1 - Summarize the following text delimited by triple \
                            backticks with 1 sentence.
                            2 - Translate the summary into French.
                            3 - List each name in the French summary.
                            4 - Output a json object that contains the following \
                            keys: french_summary, num_names.

                            Separate your answers with line breaks.

                            Text:
                            ```{text}```
                            """         
                  As we can see, it includs multi-task to do.
                  prompt_2 = f"""
                                Your task is to perform the following actions: 
                                1 - Summarize the following text delimited by 
                                <> with 1 sentence.
                                2 - Translate the summary into French.
                                3 - List each name in the French summary.
                                4 - Output a json object that contains the 
                                following keys: french_summary, num_names.

                                Use the following format:
                                Text: <text to summarize>
                                Summary: <summary>
                                Translation: <summary translation>
                                Names: <list of names in summary>
                                Output JSON: <json with summary and num_names>

                                Text: <{text}>
                              """ 
                  As we can see, in this example of prompting, we asked the model to generate an output  
                  with a specified format.

        Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion 
        prompt = f"""
                    Your task is to determine if the student's solution \
                    is correct or not.
                    To solve the problem do the following:
                    - First, work out your own solution to the problem including the final total. 
                    - Then compare your solution to the student's solution \ 
                    and evaluate if the student's solution is correct or not. 
                    Don't decide if the student's solution is correct until 
                    you have done the problem yourself.

                    Use the following format:
                    Question:
                    ```
                    question here
                    ```
                    Student's solution:
                    ```
                    student's solution here
                    ```
                    Actual solution:
                    ```
                    steps to work out the solution and your solution here
                    ```
                    Is the student's solution the same as actual solution \
                    just calculated:
                    ```
                    yes or no
                    ```
                    Student grade:
                    ```
                    correct or incorrect
                    ```

                    Question:
                    ```
                    I'm building a solar power installation and I need help \
                    working out the financials. 
                    - Land costs $100 / square foot
                    - I can buy solar panels for $250 / square foot
                    - I negotiated a contract for maintenance that will cost \
                    me a flat $100k per year, and an additional $10 / square \
                    foot
                    What is the total cost for the first year of operations \
                    as a function of the number of square feet.
                    ``` 
                    Student's solution:
                    ```
                    Let x be the size of the installation in square feet.
                    Costs:
                    1. Land cost: 100x
                    2. Solar panel cost: 250x
                    3. Maintenance cost: 100,000 + 100x
                    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
                    ```
                    Actual solution:
                  """
    ==================================================================================================

    The really impotant thing in prompting is that we must heavily consider is its "Hallucinations". It is
    one of the bigest limitation of model.

    ==================================================================================================

    Iterative Prompt Development.

    The one of the other way of prompting is thinking iterativly. This method is like developing an algorithm
    has several steps including Idea, Implementation, Experimental result, and Error Analysis. With this
    mindset we will able to reach our consiquence.
    In the following we will see how we can reach to desire result by iteratively modifing our prompt;

    Our task is to The description is intended for furniture retailers.

    fact_sheet_chair = """
                        OVERVIEW
                        - Part of a beautiful family of mid-century inspired office furniture, 
                        including filing cabinets, desks, bookcases, meeting tables, and more.
                        - Several options of shell color and base finishes.
                        - Available with plastic back and front upholstery (SWC-100) 
                        or full upholstery (SWC-110) in 10 fabric and 6 leather options.
                        - Base finish options are: stainless steel, matte black, 
                        gloss white, or chrome.
                        - Chair is available with or without armrests.
                        - Suitable for home or business settings.
                        - Qualified for contract use.

                        CONSTRUCTION
                        - 5-wheel plastic coated aluminum base.
                        - Pneumatic chair adjust for easy raise/lower action.

                        DIMENSIONS
                        - WIDTH 53 CM | 20.87”
                        - DEPTH 51 CM | 20.08”
                        - HEIGHT 80 CM | 31.50”
                        - SEAT HEIGHT 44 CM | 17.32”
                        - SEAT DEPTH 41 CM | 16.14”

                        OPTIONS
                        - Soft or hard-floor caster options.
                        - Two choices of seat foam densities: 
                        medium (1.8 lb/ft3) or high (2.8 lb/ft3)
                        - Armless or 8 position PU armrests 

                        MATERIALS
                        SHELL BASE GLIDER
                        - Cast Aluminum with modified nylon PA6/PA66 coating.
                        - Shell thickness: 10 mm.
                        SEAT
                        - HD36 foam

                        COUNTRY OF ORIGIN
                        - Italy
                        """ 
    Our First prompt:
        prompt = f"""
                    Your task is to help a marketing team create a 
                    description for a retail website of a product based 
                    on a technical fact sheet.

                    Write a product description based on the information 
                    provided in the technical specifications delimited by 
                    triple backticks.

                    Technical specifications: ```{fact_sheet_chair}```
                 """                    
        By running this prompt we will achieve to output but maybe it can be a little bit long output. So,
        we can make a limitation in first prompt to solve our first error.
    
    Our Second prompt:
        prompt = f"""
                    Your task is to help a marketing team create a 
                    description for a retail website of a product based 
                    on a technical fact sheet.

                    Write a product description based on the information 
                    provided in the technical specifications delimited by 
                    triple backticks.

                    Use at most 50 words.

                    Technical specifications: ```{fact_sheet_chair}```
                  """
        As we can see, by adding a line of limitation our output will be limitied to specified number of 
        words, sentences, or characters. But, this fact should be intended; the number of them sometimes will 
        not be the same as the number we desire.
        In the next step, we will ask it to focus on the aspects that are relevant to the intended audience.

    Our 3rd  prompt:
        prompt = f"""
                    Your task is to help a marketing team create a 
                    description for a retail website of a product based 
                    on a technical fact sheet.

                    Write a product description based on the information 
                    provided in the technical specifications delimited by 
                    triple backticks.

                    The description is intended for furniture retailers, 
                    so should be technical in nature and focus on the 
                    materials the product is constructed from.

                    At the end of the description, include every 7-character 
                    Product ID in the technical specification.

                    Use at most 50 words.

                    Technical specifications: ```{fact_sheet_chair}```
                 """
        Here, by adding some other sentence, we will be able to force the model to return our intended
        desire. In the next, we will extent our desire by asking it to extract information and organize 
        it in a table


    Our 4rd prompt:      
        prompt = f"""
                    Your task is to help a marketing team create a 
                    description for a retail website of a product based 
                    on a technical fact sheet.

                    Write a product description based on the information 
                    provided in the technical specifications delimited by 
                    triple backticks.

                    The description is intended for furniture retailers, 
                    so should be technical in nature and focus on the 
                    materials the product is constructed from.

                    At the end of the description, include every 7-character 
                    Product ID in the technical specification.

                    After the description, include a table that gives the 
                    product's dimensions. The table should have two columns.
                    In the first column include the name of the dimension. 
                    In the second column include the measurements in inches only.

                    Give the table the title 'Product Dimensions'.

                    Format everything as HTML that can be used in a website. 
                    Place the description in a <div> element.

                    Technical specifications: ```{fact_sheet_chair}```
                """
    ===============================================================================================

    Summarizing:

    To Summarize a text by LLMs we should consider this fact, what exactly we want. I mean our aim is 
    extracting a specific information from the text or just summarizing!!
    So, We should consider two espect of this majore; 1- getting brief explanation (summarizing) 
    2- extracting information beside its brief explantion.
    
    Keywords: generate a summary, summarize the text/review/article, 

    In the following some examples of summarization and one extracting information will be explained;

        Summarize with a word/sentence/character limit:
            prompt = f"""
                        Your task is to generate a short summary of a product \
                        review from an ecommerce site. 

                        Summarize the review below, delimited by triple 
                        backticks, in at most 30 words. 

                        Review: ```{prod_review}```
                      """
            As we can see, we can be puted this sort of prompt in specificity based prompting cluster.
            The prompt include commande and giudence help model to focus on our intention.

        Summarize with a focus on specific aspects of text (shipping and delivery):
            prompt = f"""
                        Your task is to generate a short summary of a product \
                        review from an ecommerce site to give feedback to the \
                        Shipping deparmtment. 

                        Summarize the review below, delimited by triple 
                        backticks, in at most 30 words, and focusing on any aspects \
                        that mention shipping and delivery of the product. 

                        Review: ```{prod_review}```
            
                      """  
            As we can see, The prompt wrote by focusing on specific aspect of text. the key word of this 
            aspect has repeated intelligently. 

        Summarize with a focus on price and value:

        It is important to know aspects like price, value, or things that are fix cann't be summarized. 
        we just need to say "Extract ..."
        Threfore,
            prompt = f"""
                        Your task is to extract relevant information from \ 
                        a product review from an ecommerce site to give \
                        feedback to the Shipping department. 

                        From the review below, delimited by triple quotes \
                        extract the information relevant to shipping and \ 
                        delivery. Limit to 30 words. 

                        Review: ```{prod_review}```
                      """
    ==============================================================================================================


    Inferring:

    Infering is one of the other majore we can use to extract information by LLM. In this majore includes,
    sentiment analysis- Identification of emotions, angry- extracting names by reviewing, infering topics.

    Sentiment (positive/negative):
        prompt = f"""
                    What is the sentiment of the following product review, 
                    which is delimited with triple backticks?

                    Give your answer as a single word, either "positive" \
                    or "negative".

                    Review text: ```{lamp_review}```
                    """

    Identify types of emotions:
        prompt = f"""
                    Identify a list of emotions that the writer of the \
                    following review is expressing. Include no more than \
                    five items in the list. Format your answer as a list of \
                    lower-case words separated by commas.

                    Review text: ```{lamp_review}```
                    """
    Identify anger:
        prompt = f"""
                    Is the writer of the following review expressing anger?\
                    The review is delimited with triple backticks. \
                    Give your answer as either yes or no.

                    Review text: ```{lamp_review}```
                    
                    """
    Extract the names (for eaxample product and company) from customer reviews:
        prompt = f"""
                    Identify the following items from the review text: 
                    - Item purchased by reviewer
                    - Company that made the item

                    The review is delimited with triple backticks. \
                    Format your response as a JSON object with \
                    "Item" and "Brand" as the keys. 
                    If the information isn't present, use "unknown" \
                    as the value.
                    Make your response as short as possible.
                    
                    Review text: ```{lamp_review}```

                    """
    Infer several topics in the text:
        prompt = f"""
                    Determine five topics that are being discussed in the \
                    following text, which is delimited by triple backticks.

                    Make each item one or two words long. 

                    Format your response as a list of items separated by commas.

                    Text sample: ```{lamp_review}```
                 """
    =====================================================================================================

    Transforming:

    Transforming is the other majore that LLMs can helps us. This area includes Translating human language,
    translating machine language (format conversion), transforming Tone of text (tone adjustment), Spell and Grammer Chec.
    In following we will pay attention to this topics by providing examples:

    Translation:
        prompt = f"""
                    Translate the following English text to Spanish: \ 
                    ```Hi, I would like to order a blender```
                  """
        prompt = f"""
                    Translate the following  text to French and Spanish
                    and English pirate: \
                    ```I want to order a basketball```
                 """

    Universal Translator:
        user_messages = [
                        "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
                        "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
                        "Il mio mouse non funziona",                                 # My mouse is not working
                        "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
                        "我的屏幕在闪烁"                                               # My screen is flashing
                        ] 
        for issue in user_messages:
                prompt = f"Tell me what language this is: ```{issue}```"
                lang = get_completion(prompt)
                print(f"Original message ({lang}): {issue}")

                prompt = f"""
                Translate the following  text to English \
                and Korean: ```{issue}```
                """

    Tone Transformation:

        prompt = f"""
                    Translate the following from slang to a business letter: 
                    'Dude, This is Joe, check out this spec on this standing lamp.'
                  """

    Format Conversion:
        data_json = { "resturant employees" :[ 
                    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
                    {"name":"Bob", "email":"bob32@gmail.com"},
                    {"name":"Jai", "email":"jai87@gmail.com"}
                ]}

        prompt = f"""
                    Translate the following python dictionary from JSON to an HTML \
                    table with column headers and title: {data_json}
                  """

    Spellcheck/Grammar check:
        text = [ 
                "The girl with the black and white puppies have a ball.",  # The girl has a ball.
                "Yolanda has her notebook.", # ok
                "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
                "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
                "Your going to need you’re notebook.",  # Homonyms
                "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
                "This phrase is to cherck chatGPT for speling abilitty"  # spelling
                ]
        for t in text:
            prompt = f"""Proofread and correct the following text
            and rewrite the corrected version. If you don't find
            and errors, just say "No errors found". Don't use 
            any punctuation around the text:
            ```{t}```"""

    ===============================================================================================================

    Expanding:

    Customize the automated reply to a customer email:
        prompt = f"""
                    You are a customer service AI assistant.
                    Your task is to send an email reply to a valued customer.
                    Given the customer email delimited by ```, \
                    Generate a reply to thank the customer for their review.
                    If the sentiment is positive or neutral, thank them for \
                    their review.
                    If the sentiment is negative, apologize and suggest that \
                    they can reach out to customer service. 
                    Make sure to use specific details from the review.
                    Write in a concise and professional tone.
                    Sign the email as `AI customer agent`.
                    Customer review: ```{review}```
                    Review sentiment: {sentiment}
                  """
        prompt = f"""
                    You are a customer service AI assistant.
                    Your task is to send an email reply to a valued customer.
                    Given the customer email delimited by ```, \
                    Generate a reply to thank the customer for their review.
                    If the sentiment is positive or neutral, thank them for \
                    their review.
                    If the sentiment is negative, apologize and suggest that \
                    they can reach out to customer service. 
                    Make sure to use specific details from the review.
                    Write in a concise and professional tone.
                    Sign the email as `AI customer agent`.
                    Customer review: ```{review}```
                    Review sentiment: {sentiment}
                 """




'''     
