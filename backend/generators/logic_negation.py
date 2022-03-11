import openai
import random
class question_generator:
        def __init__(self):
            self.gen_con_Q = "The negation of a statement is the opposite of the given mathematical statement. To negate a statement of the form If A, then B we should replace it with the statement A and negation of B. Consider the statement If I am rich, then I am happy. For this statement to be false, I would need to be rich and not happy. If A is the statement I am rich and B is the statement I am happy, then the negation of this statement is I am rich, and I am not happy. Write examples of negation of the given statements. \n\nstatement:  If I fail the exam, then my family will reject me.\nnegation: I failed the exam and my family did not reject me.\n\nstatement: If I am going to the party, then I am going to the library.\nnegation: I am going to the party and I am not going to the library.\n\nstatement: If I eat all my vegetables, then I will grow tall.\nnegation: I ate all my vegetables and I did not grow tall.\n\nstatement: "
            self.gen_con_S = "Conditional sentences are statements discussing known factors or hypothetical situations and their consequences. Complete conditional sentences contain a conditional clause (often referred to as the if-clause) and the consequence. If, then” statements require commas to separate the two clauses that result. If I use correct punctuation, then I will include commas where necessary. Continue to generate sentences conditional sentences shown in the example: \n\n1.If it rains this afternoon, then yesterday's weather forecast was wrong\n2. I would travel around the world if I won the lottery.\n2. If I won the lottery, then I would travel around the world.\n3. If water reaches 100 degrees, then it boils.\n4."
            self.gen_statement = "A statement as such is a claim that something is or is not true. A statement is true if what it claims is true, and false if what it claims is not true. It must be possible to determine whether a statement is true or false. When we assert that people have bones, we can know with certainty that it is true, and therefore it qualifies as a statement. Generate examples of statements:\n\n1. Tailgating is a top cause of car accidents.\n2. It is raining at this moment.\n3. The trains are always late.\n4."
            self.gen_neg = "Negation is a process to determine what the opposite of a given statement is. One thing to keep in mind is that if a statement is true, then its negation is false (and if a statement is false, then its negation is true). Write examples of negation of the given statements. \n\nstatement:  I like you.\nnegation: I hate you.\nstatement: My family is going on a trip.\nnegation: My family is not going on a trip.\nstatement: It is raining today.\nnegation: I is not raining today.\nstatement: "
            self.gen_uni_Q = "The negation of a statement is the opposite of the given mathematical statement. In general, when negating a statement involving (for all) or (for every), the phrase (for all) gets replaced with (there exists). Generate negations based on the statements:\n\nstatement:  For all integers n, either n is even or n is odd.\nnegation: There exists an integer n, so that n is not even and n is not odd.\nstatement: For all universities, there are professors working in them.\nnegation: There exists am university, so that there is no professor teaching in it.\nstatement: For every fruit,  there exists a smoothie made from it.\nnegation: There is a fruit, so that there is no smoothie made from it.\nstatement:"
            self.gen_uni_S = "In mathematical logic, a universal quantification is a type of quantifier, a logical constant which is interpreted as (for all). It expresses that a predicate can be satisfied by every member of a domain of discourse. In general, when creating this statement, we start with for all x and continue with stating what statement is true for all x. Generate these examples of for all statements based on the examples:\n\n1.  For all integers n, either n is even or n is odd.\n2. For all universities, there are professors working in them.\n3. For every fruit, there exists a smoothie made from it.\n4. "
            self.gen_exi_S  ="In mathematical logic, a existencial quantification is a type of quantifier, a logical constant which is interpreted as (There is) or (There exists). It expresses that a predicate can be satisfied by at least one member of a domain of discourse. In general, when creating this statement, we start with there is (something) and continue with stating what statement is true for at least one (something). Generate these examples of for all statements based on the examples: \n\n1.  There exists an integer n so that n is even or n is odd.\n2.  There is a hero, such that he possesses a legendary sword.\n3. There exists a student at UCL, such that he was accepted into Oxford.\n4."
            self.gen_exi_Q  = "The negation of a statement is the opposite of the given mathematical statement. In general, when negating a statement involving (there exist) or (there is), the phrase (there exist) gets replaced with (for all). The following statement is then the negation of the original statement. The statement is thus existential and not universal. Generate negations based on the statements: \n\nstatement:  There exists an integer n so that n is even or n is odd.\nnegation: For all integers n, n not even and n is not odd.\nstatement:  There is a hero, such that he possesses a legendary sword.\nnegation: for all heroes, none of them possesses a legendary sword.\nstatement: There exists a student at UCL, such that he was accepted into Oxford. \nnegation: For every student at UCL, none got accepted into Oxford.\nstatement:"
            self.alter_txt = "Slightly alter the subject of the statement so the new alteration resembles it but has a different meaning. Generate new alterations based on the given statement.\n\nStatement: All the boys wanted to win the match.\nAlteration: All the boys from my high school wanted to win the marathon.\nStatement: If I miss my train, then I will take the bus.\nAlteration: If I miss my bus, then I will take a taxi.\nStatement: This joke terrified and amused the internet.\nAlteration: This news terrified and amused the people on the internet.\nStatement:"
        
        def gpt3(self,stext, temp, tokens):
            openai.api_key = "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"
            response = openai.Completion.create(
                engine="davinci-instruct-beta",
                prompt=stext,
                temperature = temp,
                max_tokens = tokens,
                top_p=1,
                frequency_penalty = 0,
                presence_penalty = 0
            )
            content = response.choices[0].text.split(".")
            return content
        
        def if_sentence_check(self):   
            while(True):
                response = self.gpt3(self.gen_con_S,0.95,40)[0].split(" ")
                if_num = 0
                then_num = 0
                for i in response:
                    if (i.lower() == "if"):
                        if_num+=1
                    if (i.lower() == "then"):
                        then_num+=1
                if (if_num==1 and then_num==1):
                    return(' '.join(word for word in response[1:]))
                
        def if_question_check(self,txt):    
            check = True
            while(check):
                response = self.gpt3(self.gen_con_Q+txt+"\nnegation:",0.78,45)[0].split(" ")
                and_num = 0
                not_num = 0
                for i in response:
                    if (i.lower() == "and"):
                        and_num+=1
                    if (i.lower() == "not"):
                        not_num+=1
                        if(and_num<1 and not_num==1):
                            not_num=2
                if (and_num==1 and not_num<2):
                    check = False
            return([txt,' '.join(word for word in response[0:])])
        
        def statement_check(self):    
            response =self.gpt3(self.gen_statement,0.9,10)[0].split(" ")
            return(' '.join(word for word in response[1:]))
        
        def neg_check(self,txt):
            if ("." not in txt):
                txt = (txt + ".")
            while(True):
                response =self.gpt3(self.gen_neg+txt+"\nnegation:",0.85,25)[0].split(" ")
                neg = ' '.join(word for word in response[1:])
                if(neg !=txt):
                    return(neg.replace(".", ""))
        
        def generate_AorB(self): 
            A = self.statement_check()
            B = self.statement_check().lower()
            txt = str(A+" or "+B)
            A_neg = self.neg_check(A)
            B_neg = self.neg_check(B)
            response = str(A_neg+" and "+B_neg)
            return [txt,response]

        def generate_AandB(self): 
            A = self.statement_check()
            B = self.statement_check().lower()
            txt = str(A+" and "+B)
            A_neg = self.neg_check(A)
            B_neg = self.neg_check(B)
            response = str(A_neg+" or "+B_neg)
            return [txt,response]

        def forall_sentence_check(self):   
            while(True):
                response =self.gpt3(self.gen_uni_S,0.95,30)[0].split(" ")
                for_num = 0
                every_num = 0
                n_num = 0
                for i in response:
                    if (i.lower() == "for"):
                        for_num+=1
                    if (i.lower() == "every"):
                        every_num+=1
                    if (i.lower() == "\n"):
                        n_num+=1
                if (for_num>=1 and every_num>=1 and n_num<1):
                    return(' '.join(word for word in response[1:]))

        def forall_question_check(self,txt):    
            check = True
            while(check):
                response =self.gpt3(str(self.gen_uni_Q)+str(txt)+"\nnegation:",0.7,30)
                response = response[0].split(" ")
                there_num = 0
                such_num = 0
                for i in response:
                    if (i.lower() == "there"):
                        there_num+=1
                if (there_num>=1):
                    check = False
            return([txt,' '.join(word for word in response[1:])])
    
        def thereis_sentence_check(self):   
            while(True):
                response =self.gpt3(self.gen_exi_S,0.9,30)[0].split(" ")
                there_num = 0
                n_num = 0
                for i in response:
                    if (i.lower() == "there"):
                        there_num+=1
                    if (i.lower() == "\n"):
                        n_num+=1
                if (there_num>=1 and n_num<1):
                    return(' '.join(word for word in response[1:]))
                
        def thereis_question_check(self,txt):    
            check = True
            while(check):
                response =self.gpt3(str(self.gen_exi_Q)+str(txt)+"\nnegation:",0.8,30)
                if ("for " in response[0].lower() and " all " in response[0].lower() and  "\n" not in response[0].lower()):
                    return([txt,response[0]])
        
        def alter_check(self,txt):
            if ("." not in txt):
                txt = (txt + ".")
            while(True):
                response =self.gpt3(str(self.alter_txt)+str(txt)+"\nAlteration:",0.9,25)[0].split(" ")
                neg = ' '.join(word for word in response[1:])
                if(neg !=txt):
                    return(neg.replace(".", ""))

        def answer_corruptor(self,txt):
            three_bad_an = [txt]
            if(" or " in txt):
                three_bad_an.append(txt.replace(" or ", " and "))

            if(" and " in txt):
                three_bad_an.append(txt.replace(" and ", " or "))

            if(" for " not in txt):
                three_bad_an.append(self.thereis_question_check(txt)[1])

            if(" there " not in txt):
                three_bad_an.append(self.forall_question_check(txt)[1])
            three_bad_an.append(self.neg_check(txt))
            while(len(set(three_bad_an))<4):
                 three_bad_an.append(self.alter_check(txt))
            three_bad_an = list(set(three_bad_an))
            three_bad_an.remove(txt)
            return (random.sample(three_bad_an, 3))
        
        def main(self,x):
            check = True
            while(check):
                if(x == 1):
                    question = self.if_sentence_check()
                    c_answer = self.if_question_check(question)[1]
                elif(x == 2):
                    lst = self.generate_AorB()
                    question = lst[0]
                    c_answer = lst[1]
                elif(x == 3):
                    lst = self.generate_AandB()
                    question = lst[0]
                    c_answer = lst[1]
                elif(x==4):
                    question = self.forall_sentence_check()
                    c_answer = self.forall_question_check(question)[1]
                elif(x==5):
                    question = self.forall_sentence_check()
                    c_answer = self.forall_question_check(question)[1]
                elif(x==6):
                    question = self.thereis_sentence_check()
                    c_answer = self.thereis_question_check(question)[1]
                if("\n" not in question and "\n" not in c_answer):
                    check = False
            lst = self.answer_corruptor(c_answer)
            return [question,c_answer,lst]

            
