if __name__ == '__main__':

    # import random
    from operator import itemgetter

    # def rand_dict(n):
    #     d = {}
    #     for i in range (n):
    #         d[random.randint(0, 20)] = random.randint(0, 20)
    #     return d
    #
    # def rev_dict(d):
    #     d1 = {}
    #     for (key, value) in d.items():
    #         d1[value] = key
    #     return d1
    #
    # d = rand_dict(14)
    # d1 = rev_dict(d)
    # print(d)
    # print (d1)

    def k_most_popular_words(string, k=3):
        list_ = string.split(" ")
        counter = {}

        # for word in list_:
        #     counter[word] = counter.get(word, 0) + 1

        for i in range(len(list_)):
            counter[list_[i]] = 0

        for word in list_:
            counter[word] += 1

        print(counter)

        list_of_tuples = list(counter.items())
        list_of_tuples.sort(key=itemgetter(1), reverse=True)
        print(list_of_tuples[0:k])



    string_ = "e-mails the only only The is is the of only of content content is of content e-mails of information the is of words words a"
    k_most_popular_words(string_)
