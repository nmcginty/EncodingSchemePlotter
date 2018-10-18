import matplotlib.pyplot as plt
import numpy as np

# bits = [0,1,0,1,1,0,1,1,0,0,1,1,0,1,0]
# have each scheme function return list of bits to plot
# and text output which is list of +, - or 0

def get_sign(bit):
    return bit if bit == 0 else ('+' if bit > 0 else '-')

def nrzlScheme(bits):
    nrzl = [-1 if bit else 1 for bit in bits]
    nrzl_text = [get_sign(bit) for bit in bits]
    return np.repeat(nrzl, 2), nrzl_text

def pseudoternaryScheme(bits):
    pseudoternary = [0 if bits[0] else -1] 
    pseudoternary_text = [0 if bits[0] else '-']
    prev_zero_bit = 1 if bits[0] else -1

    for bit in bits[1:]:
        prev_zero_bit *= 1 if bit else -1
        next_level = 0 if bit else prev_zero_bit
        pseudoternary.append(next_level)
        pseudoternary_text.append(get_sign(bit))
        
    return np.repeat(pseudoternary, 2), pseudoternary_text

def mlt3Scheme(bits):
    mlt3 = [0 if bits[0] else 1] 
    mlt3_text = [0 if bits[0] else '+']
    prev_bit, last_non_zero_level = mlt3[0], mlt3[0]

    for bit in bits[1:]:

        if bit == 1:
            if prev_bit: # 1 or -1
                bit = 0
            else: # current level is 0
                if last_non_zero_level == 1:
                    bit -= 1
                elif last_non_zero_level == 0:
                    bit = 1
                elif last_non_zero_level == -1:
                    bit += 1

                bit += -1 if last_non_zero_level > -1 else 1
                last_non_zero_level = bit

        prev_bit = bit

        mlt3.append(bit)
        mlt3_text.append(get_sign(bit))
        
    return np.repeat(mlt3, 2), mlt3_text

def axis_lines():
    pass

def my_lines(ax, pos, *args, **kwargs):

    # print([arg for arg in args])
    # print([kwargs for kwargs in kwargs])

    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

def plotSchemes(bits):
    print("BITS", bits)

    nrzl, nrzl_text = nrzlScheme(bits)
    pseudoternary, pseudoternary_text = pseudoternaryScheme(bits)
    mlt3, mlt3_text = mlt3Scheme(bits)

    data = np.repeat(bits, 2) # just doubles element in sequnce
    # print("DATA", data)

    t = 0.5 * np.arange(len(data))
    print("DATA", data)
    print("T", t)
    # plt.hold(True) # apparently deprecated so bad!!!!

    # # linewidth is literally tickness of line
    # second argument is range of numbers where a line will be drawn on appropriate axis
    # remainder of arguements will resolve to args and kwargs
    my_lines('x', range(16), color='.5', linewidth=2) 
    my_lines('y', [1, 5, 9, 13], color='.5', linewidth=2)
    #plt.step(x, y, color, args)
    plt.step(t, nrzl + 9, 'g', linewidth = 2, where='post', label='nrzl')
    plt.step(t, pseudoternary + 5, 'b', linewidth = 2, where='post', label='pseudoternary')
    plt.step(t, mlt3 + 1, 'r', linewidth = 2, where='post', label='mlt3')
    plt.legend(loc='upper right')

    plt.ylim([-2, 17])

    for tbit, bit in enumerate(bits):
        plt.text(tbit + 0.5, 11, str(bit))
        plt.text(tbit + 0.5, 7, str(bit))
        plt.text(tbit + 0.5, 3, str(bit))

    plt.gca().axis('off')
    plt.savefig('schemePlots.png')
    plt.show()

if __name__ == "__main__":
    # bits = [0,1,0,1,1,0,1,1,0,0,1,1,0,1,0] # test 1
    # bits = [1,1,0,0,1,1,0,0,1,0,1,0,1,0,1]
    # bits = # test 2
    # bits = [0]*15 
    bits = [1]*15
    # bits = [0, 1]*8
    # bits.pop()
    
    plotSchemes(bits)