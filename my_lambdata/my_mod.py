# my_lambdata/my_mod.py


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100



# Single function to take a list, turn it into a series and add it to a dataframe as a new column
def list_into_df(lst, dtf):
    new_col = pd.Series(lst)
    df_new = pd.concat([dtf, new_col], axis=1)
    return df_new



# this code breaks our ability to import enlarge from other files
#
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))




if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))