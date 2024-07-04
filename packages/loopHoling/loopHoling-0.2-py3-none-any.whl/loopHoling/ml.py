def code1():

    codee = """import pandas as pd
                import numpy as np
                data = pd.read_csv('C:/Users/Students/Desktop/trainingexamples.csv')
                ass = data
                features = np.array(data)[:,:-1]
                print("features in the database:\n",features)
                target = np.array(data)[:,-1]
                print("target concept:\n",target)
                for i,val in enumerate(target):
                    if val == 'Yes':
                        hypothesis = features[i].copy()
                        break
                print(hypothesis)
                for i,val in enumerate(features):
                    if target[i] == 'Yes':
                        for x in range (len(hypothesis)):
                            if val[x] != hypothesis[x]:
                                hypothesis[x] = '?'
                                
                print(hypothesis)"""
    return codee


def code2():

    codee = """import numpy as np
            import pandas as pd
            data = pd.DataFrame(data=pd.read_csv('data.csv'))

            concepts = np.array(data.iloc[:,0:-1])
            target= np.array(data.iloc[:,-1])
            def learn(concepts, target):
                specific_h = concepts[0].copy()
                general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
                for i,h in enumerate(concepts):
                    if target[i] == 'yes':
                        for x in range(len(specific_h)):
                            if h[x]!= specific_h[x]:
                                specific_h[x] = '?'
                                general_h[x][x] = '?'
                    if target[i] == 'no':
                        for x in range(len(specific_h)):
                            if h[x] != specific_h[x] :
                                general_h[x][x] = specific_h[x]
                            else:
                                general_h[x][x] = '?'
                indices = [i for i, val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
                for i in indices:
                    general_h.remove(['?','?','?','?','?','?'])
                return specific_h, general_h
            s_final, g_final = learn(concepts, target)
            print('Final S: ', s_final, sep="\n")
            print('Final G: ', g_final, sep="\n")"""
    return codee

def code3():

    codee = """import numpy as np 
            import pandas as pd
            dataset = pd.read_csv('C:/Users/Students/Desktop/data.csv')
            print(dataset)
            def entropy(target):
                elements,counts = np.unique(target,return_counts = True)
                entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts))for i in range(len(elements))])
                return entropy
            def InfoGain(data,split_attribute_name,target_name = "Decision"):
                total_entropy = entropy(data[target_name])
                vals,counts= np.unique(data[split_attribute_name],return_counts=True)
                Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name])for i in range(len(vals))])
                InfoGain = total_entropy-Weighted_Entropy
                return InfoGain
            def ID3(data,originaldata,features,target_attribute_name="Decision",parent_node_class = None):
                if len(np.unique(data[target_attribute_name]))<=1:
                    return np.unique(data[target_attribute_name])[0]
                elif len(data) == 0:
                    return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name],return_counts = True)[1])]
                elif len(features)==0:
                    return parent_node_class
                else:
                    parent_node_class=np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts = True)[1])]
                    items_values=[InfoGain(data,feature,target_attribute_name) for feature in  features]
                    best_feature_index = np.argmax(items_values)
                    best_feature = features[best_feature_index]
                tree = {best_feature:{}}
                features =[i for i in features if i != best_feature]
                for value in np.unique(data[best_feature]):
                    value = value
                    sub_data = data.where(data[best_feature]== value).dropna()
                    subtree = ID3(sub_data,dataset,features,target_attribute_name,parent_node_class)
                    tree[best_feature][value]= subtree
                return(tree)
            tree = ID3(dataset,dataset,dataset.columns[:-1])
            print('\n Display Tress:\n',tree)"""
    return codee

def code4():

    codee = """import numpy as np 

            x = np.array(([2,9],[1,5],[3,6]),dtype=float)
            y = np.array(([92],[86],[89]),dtype=float)

            x = x/np.amax(x,axis=0)
            y = y/100

            def sigmoid(x):
                return 1/(1+np.exp(-x))
                        
            def derivatives_sigmoid(x):
                return x*(1-x)

            epoch = 900
            lr = 1.5

            inputlayer_neuron = 2
            hiddenlayer_neuron = 3
            output_neuron = 1
            wh = np.random.uniform(size =(inputlayer_neuron,hiddenlayer_neuron))
            bh = np.random.uniform(size =(1,hiddenlayer_neuron))
            wout = np.random.uniform(size =(hiddenlayer_neuron,output_neuron))
            bout = np.random.uniform(size =(1,output_neuron))

            for i in range(epoch):
                hinp1 = np.dot(x,wh)
                hinp = hinp1 + bh
                hlayer_act  = sigmoid(hinp)
                outinp1 = np.dot(hlayer_act,wout)
                outinp = outinp1 + bout
                output = sigmoid(outinp)
                EO = y-output
                outgrad = derivatives_sigmoid(output)
                
                d_output = EO*outgrad
                EH = d_output.dot(wout.T)
                hiddengrad = derivatives_sigmoid(hlayer_act)
                

            d_hiddenlayer =EH * hiddengrad

            wout += hlayer_act.T.dot(d_output)*lr
            bout += np.sum(d_output,axis=0,keepdims=True)*lr
            wh += x.T.dot(d_hiddenlayer)*lr
            bh += np.sum(d_hiddenlayer,axis = 0, keepdims = True)*lr
            print("input: \n " + str(x))
            print("Actual Output : \n" + str(y))
            print("Predicted output: \n",output)"""
    return codee

def code5():

    codee = """import pandas as pd
            from sklearn import tree
            from sklearn.preprocessing import LabelEncoder
            from sklearn.naive_bayes import GaussianNB

            data = pd.read_csv('tennisdata.csv')
            print("The first 5 Values of data is :\n", data.head())

            X = data.iloc[:, :-1]
            print("\nThe First 5 values of the train data is\n", X.head())
            y = data.iloc[:, -1]
            print("\nThe First 5 values of train output is\n", y.head())

            le_outlook = LabelEncoder()
            X.Outlook = le_outlook.fit_transform(X.Outlook)
            le_Temp = LabelEncoder()
            X.Temp= le_Temp.fit_transform(X.Temp)
            le_Humidity = LabelEncoder()
            X.Humidity = le_Humidity.fit_transform(X.Humidity)
            le_Wind = LabelEncoder()
            X.Wind = le_Wind.fit_transform(X.Wind)
            print("\nNow the Train output is\n", X.head())
            le_PlayTennis = LabelEncoder()
            y = le_PlayTennis.fit_transform(y)

            print("\nNow the Train output is\n",y)
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.50)
            classifier = GaussianNB()
            classifier.fit(X_train, y_train)

            from sklearn.metrics import accuracy_score
            print("Accuracy is:", accuracy_score(classifier.predict(X_train), y_train))
            print("Accuracy is:", accuracy_score(classifier.predict(X_test), y_test))"""
    return codee

