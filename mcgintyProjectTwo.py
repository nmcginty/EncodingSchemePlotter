import matplotlib.pyplot as plt
import numpy as np

# bits = [0,1,0,1,1,0,1,1,0,0,1,1,0,1,0]
# have each scheme function return list of bits to plot
# and text output which is list of +, - or 0

def get_sign(bit):
    return str(bit) if bit == 0 else ('+' if bit > 0 else '-')

def nrzlScheme(bits):
    nrzl_level = [-1 if bit else 1 for bit in bits]
    nrzl_text = [get_sign(level) for level in nrzl_level]
    return np.repeat(nrzl_level, 2), nrzl_text

def pseudoternaryScheme(bits):
    pseudoternary_levels = [0 if bits[0] else -1] 
    pseudoternary_text = [str(0) if bits[0] else '-']
    last_zero_level = 1 if bits[0] else -1

    for bit in bits[1:]:
        last_zero_level *= 1 if bit else -1
        next_level = 0 if bit else last_zero_level
        pseudoternary_levels.append(next_level)
        pseudoternary_text.append(get_sign(next_level))
        
    return np.repeat(pseudoternary_levels, 2), pseudoternary_text

def mlt3Scheme(bits):
    mlt3_levels = [0 if bits[0] else 1] 
    mlt3_text = [0 if bits[0] else '+']
    current_level, last_non_zero_level = mlt3_levels[0], 1
    
    for next_bit in bits[1:]:
        
        next_level = current_level # if 0 no transition 
        if next_bit == 1:
            if current_level == 0: # 1 or -1
                last_non_zero_level *= -1
                next_level = last_non_zero_level
            else: # current level is 1 or -1
                next_level = 0

        current_level = next_level
        mlt3_levels.append(next_level)
        mlt3_text.append(get_sign(next_level))

    # mlt3_levels.append(mlt3_levels[-1])
    return np.repeat(mlt3_levels, 2), mlt3_text

def createAxes(ax, pos, *args, **kwargs):

    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

def plotSchemes(bits):

    nrzl_levels, nrzl_text = nrzlScheme(bits)
    pseudoternary_levels, pseudoternary_text = pseudoternaryScheme(bits)
    mlt3_levels, mlt3_text = mlt3Scheme(bits)

    nrzl_levels = np.append(nrzl_levels, nrzl_levels[-1])
    pseudoternary_levels = np.append(pseudoternary_levels, pseudoternary_levels[-1:])
    mlt3_levels = np.append(mlt3_levels, mlt3_levels[-1:])
    print([str(bit) for bit in bits], "Bits")
    print(nrzl_text, "NRZ-L")
    print(pseudoternary_text, "Pseudoternary")
    print(mlt3_text, "MLT-3")
    # bits.append(bits[-1])
    data = np.repeat(bits, 2) # just doubles element in sequnce
    t = 0.5 * np.arange(len(data))
    t = np.append(t, t[-1]+0.5)

    # # linewidth is literally tickness of line
    # second argument is range of numbers where a line will be drawn on appropriate axis
    # remainder of arguements will resolve to args and kwargs
    createAxes('x', range(len(bits)+1), color='.5', linewidth=2) 
    createAxes('y', [1, 5, 9, 13], color='.5', linewidth=2)
    #plt.step(x, y, color, args)
    plt.step(t, nrzl_levels + 9, 'green', linewidth = 2, where='post', label='NRZ=L')
    plt.step(t, pseudoternary_levels + 5, 'blue', linewidth = 2, where='post', label='Pseudoternary')
    plt.step(t, mlt3_levels + 1, 'red', linewidth = 2, where='post', label='MLT-3')
    plt.legend(loc='upper right', prop={'size': 10})

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
    bits = [1,1,0,0,1,1,0,0,1,0,1,0,1,0,1] # test 2
    # bits = [0]*15 
    # bits = [1]*15
    # bits = [0,0,0,1,1,0,0,0]
    # bits = [0, 1]*8
    # bits.pop()

    # print("Test 1")
    print("Test 2")
    plotSchemes(bits)