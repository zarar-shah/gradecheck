def introduction(essayText):
    message = ""
    if "will argue that" in essayText or "would argue that" in essayText or " going to argue that" in essayText or "essay argues" in essayText or "main argument is that" in essayText or "paper argues" in essayText or "article argues" in essayText or "report argues" in essayText or "review argues" in essayText or " I argue" in essayText:
        # print("Introduction")
        message = message +  "You have a good thesis statement\n"
    elif "this thesis statement" in essayText or "The thesis statement" in essayText or "the thesis statement" in essayText or "This thesis statement" in essayText:
        print("Introduction")
        message = message + 'It is good that you mention your thesis statement, but it would be better to express this as an argument. For example, "This essay will argue that..."\n'
    elif "This essay will " in essayText or "I will" in essayText or "This paper" in essayText or "This article" in essayText or "In this essay" in essayText or "In this article" in essayText or "This review" in essayText or "In this book review" in essayText or "In this review" in essayText or "In this report" in essayText or "this essay will " in essayText or "In this essay" in essayText or "in this essay" in essayText or "agree with" in essayText or "strongly agree" in essayText or "In this paper" in essayText or "in this paper" in essayText or "in this report" in essayText or "in the following" in essayText or "In the following" in essayText or "argues whether" in essayText:
        print("Introduction")
        message = message + 'Thesis statement can be improved. You should have a thesis statement that clearly and explicitly states what your overall argument will be. For example, "This essay will argue that..."\n'
    else:
        print("Introduction")
        message = message + 'You are missing a thesis statement. You should have a thesis statement that clearly and explicitly states what your overall argument will be. For example, "This essay will argue that..."\n'

    if "will first" in essayText or "Finally" in essayText or "will also be" in essayText or "Lastly" in essayText or "first is going to" in essayText or "is going to first" in essayText or "would be divided" in essayText or "first part" in essayText or "Then it will" in essayText or "First, this " in essayText or "First, it " in essayText or "followed by" in essayText or "Following this" in essayText or "Next will" in essayText or "Next, it will" in essayText or "After that, it will" in essayText or "After that, I will" in essayText or "After, it will" in essayText or "At last, it will" in essayText or "After that, I will" in essayText or " been divided" in essayText or " is divided" in essayText:
        print('Introduction')
        message = message + 'You outline the structure of your essay reasonably well.\n'
    elif "will be" in essayText or "will conclude" in essayText or "concludes" in essayText or "overall conclusion" in essayText or "a conclusion" in essayText or "would be the first" in essayText or "in the following" in essayText:
        print('Introduction')
        message = message + 'Your essay outline can be improved. It would be useful for the reader to include a step-by-step overview in your introduction of how you will structure your essay.\n'
    else:
        print('Introduction')
        message = message + 'You are missing an outline of your essay. It would be useful for the reader to include a step-by-step overview in your introduction of how you will structure your essay.\n'

    return message


def Tone_and_style(essayText):
    message = ""
    if "we" in essayText or "our" in essayText or "Our " in essayText or "We" in essayText or "us" in essayText or "my" in essayText or "My" in essayText or "I think" in essayText or "mine" in essayText or "Our" in essayText or "You " in essayText or " you " in essayText or " your " in essayText or "I believe" in essayText:
        print('Tone & Style')
        message = message +  'In academic writing, do not use personal pronouns (we, us, our, you, my, I, etc.) since they will often make your essay seem more subjective and personal and less objective and formal. Try to express these sentences without personal pronouns.\n'


    if "a lot" in essayText or " lots " in essayText or ", so " in essayText or " bad " in essayText or " get " in essayText or " getting" in essayText or " big" in essayText or "A lot " in essayText or "Nowadays" in essayText or "hot topic" in essayText or " thing" in essayText or "more and more" in essayText or "More and more" in essayText or "nowadays" in essayText:
        print('Tone & Style')
        message = message + 'You use some informal and non-academic vocabulary. Examples of common non-academic vocabulary are "a lot," "so," "get," "big," "thing," "bad," "nowadays" and "more and more." Try to adopt a more formal tone when you write.\n'

    if "may" in essayText or "seem" in essayText or "appears" in essayText or "tends to" in essayText or "might " in essayText or " possible" in essayText or "likely " in essayText or "arguably" in essayText or "Arguably" in essayText or " possibly " in essayText or "Generally" in essayText or "generally" in essayText or "commonly" in essayText or "It can be " in essayText or " it can be " in essayText or "to a large extent" in essayText or "to some extent" in essayText:
        print('Tone & Style')
        message = message + 'You hedge some of your claims well.\n'
    else:
        print('Tone & Style')
        message = message + 'In academic writing, you should hedge your claims by showing more cautious language. Try to use words like "may," "might," "seems to," "likely to," "generally," "arguably," etc. to acknowledge that you might be wrong.\n'

    if "always" in essayText or "never " in essayText or "everyone" in essayText or "As we all know" in essayText or "We all know" in essayText or "everybody" in essayText or "Everyone" in essayText or "Everybody" in essayText or "Obviously" in essayText or "obviously" in essayText or " obvious " in essayText:
        print('Tone & Style')
        message = message + 'Avoid using assertive language (always, never, everybody, obviously, we all know) in your essay. Use more cautious language like "some people," "most people," "usually," "sometimes," "often," "possibly," etc. This will make it less likely that a reader will disagree with you.\n'

    if "? " in essayText:
        print('Tone & Style')
        message = message + 'In academic writing it is not common to ask questions directly to the reader. Instead of asking a question, try to begin your sentence in another way such as "It is questionable whether"\n'

    if "Take " in essayText:
        print('Tone & Style')
        message = message + 'Do not use imperatives in academic writing\n'

    if "'t" in essayText or "'ve" in essayText or "'ll" in essayText:
        print('Tone & Style')
        message = message + 'Do not use contractions or short-form in academic writing. Write out the full words eg "Do not"\n'

    if " But" in essayText or "So " in essayText or "Because" in essayText or "And " in essayText or "Besides," in essayText:
        print('Tone & Style')
        message = message + 'Avoid informal sentence starters like but, so, and, because & besides. Instead, begin sentences with more formal words, such as however, therefore, as a result, additionally and furthermore.\n'

    if "On the other hand" in essayText or " on the other hand" in essayText or "coin has two sides" in essayText or "blessing or a curse" in essayText or "tip of the iceberg" in essayText:
        print('Tone & Style')
        message = message + 'Avoid using cliches in academic writing.\n'

    if "Therefore" in essayText or "therefore" in essayText or "As a result" in essayText or "as a result" in essayText or "Consequently" in essayText or "consequently" in essayText or "Thus" in essayText or "thus" in essayText or "Similarly" in essayText or "similarly" in essayText or "Moreover" in essayText or "In addition" in essayText or "Furthermore" in essayText or "Additionally" in essayText or "Conversely" in essayText or "Specifically" in essayText or "Also, " in essayText:
        print('Structure: Coherence & Cohesion')
        message = message + 'You use some cohesive devices well to link ideas.\n'
    else:
        print('Structure: Coherence & Cohesion')
        message = message + 'Improve your cohesion by linking your ideas. To do this, add cohesive devices or connecting words in between sentences, such as "therefore," "in addition," "similarly" or "conversely" so that the reader can see how one sentence relates to a previous idea.\n'

    
    return message   



def structure(essayText):
    message = ""
    if "One of the " not in essayText and " one of the " not in essayText and " reason why " not in essayText and " reasons why" not in essayText and "Another " not in essayText and " be another " not in essayText and "One " not in essayText and " is one " not in essayText and "may be one " not in essayText and " is another " not in essayText and "A possible " not in essayText and "There are " not in essayText and "There may " not in essayText and "The other " not in essayText and "the main point" not in essayText and "The main point" not in essayText and "First" not in essayText and "Second" not in essayText:
        print('Structure: Topic Sentences')
        message = message + 'Consider improving your topic sentences so that they more effectively introduce the one main point the paragraph.\n'

    if "Therefore" not in essayText and "As a result" not in essayText and "Thus" not in essayText and "Consequently" not in essayText and "Based on the above" not in essayText and "based on the above" not in essayText:
        print('Structure: Concluding Sentences')
        message = message + 'Consider improving concluding sentences at the end of your body paragraphs so that they better summarise the one main point of the paragraph.\n'

    if "0)" in essayText or "9)" in essayText or "8)" in essayText or "7)" in essayText or "6)" in essayText or "5)" in essayText or "4)" in essayText or "3)" in essayText or "2)" in essayText or "1)" in essayText:
        print('Referencing')
        message = message + 'Your essay includes some citations in APA format. Remember to include a minimum of ____ in your final essay.\n'
    else:
        print('Referencing')
        message = message + 'Your essay seems to be missing in-text citations in APA format. Remember to include a minimum of ____ in your final essay.'

    if "[" in essayText or "]" in essayText:
        print('Referencing')
        message = message + 'You have some citations in IEEE format. Remember to include a minimum of ____ in your final essay.'
    else:
        print('Referencing')
        message = message + 'Your essay seems to be missing citations in IEEE format. Remember to include a miminum of ___ in your final essay.'

    if " said " in essayText or " says " in essayText:
        print('Referencing')
        message = message + 'Improve the quality of your reporting verbs. Instead of using says/said/thinks, use argues/demonstrates/highlights/emphasises instead.'

    if ".,(" in essayText or "., (" in essayText or ".,1" in essayText or "., 1" in essayText or ".,2" in essayText or "., 2" in essayText:
        print('Referencing')
        message = message + 'In your citations, make sure you only include the surname of the author, not their first initials.'

    return message


def word_count(essayText):
    res = len(essayText.split())
    print('Word Count: ' +str(res))
    
    message = ""
    if res < 1490:
        print('Requirements')
        message = 'Your paper is below the word limit for the SECOND DRAFT. Make sure your next draft meets the word limit'

    if res < 700:
        print('Requirements')
        message = 'Your paper is below the word limit for the FIRST DRAFT. Make sure your next draft meets the word limit'


    return message
