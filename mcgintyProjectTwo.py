import matplotlib.pyplot as plt
import numpy as np

# each scheme function return lists of bits to plot
# and text output which is list of +, - or 0
# assume scheme starts positive if neccessary

# determine sign of bit, either +, - or 0
def get_sign(bit):
    return str(bit) if bit == 0 else ('+' if bit > 0 else '-')

# non-return to zero scheme
# signal is positive when bit is 0, negative when bit is 1
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

# 
# we arbitrarily assume last_non_zero_level is positive or 1
def mlt3Scheme(bits):
    mlt3_levels = [0 if bits[0] else 1] 
    mlt3_text = [str(0) if bits[0] else '+']
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

    return np.repeat(mlt3_levels, 2), mlt3_text


# plots line at each value in lines on appropriate axis
def createAxes(axis, lines, *args, **kwargs):

    if axis == 'x':
        for line in lines:
            plt.axvline(line, *args, **kwargs)
    else: # y
        for line in lines:
            plt.axhline(line, *args, **kwargs)

def plotSchemes(bits):

    nrzl_levels, nrzl_text = nrzlScheme(bits)
    pseudoternary_levels, pseudoternary_text = pseudoternaryScheme(bits)
    mlt3_levels, mlt3_text = mlt3Scheme(bits)

    # add extra bit equal to last in each scheme
    # this is required to extend the plotter to fill the y axis slice
    nrzl_levels = np.append(nrzl_levels, nrzl_levels[-1])
    pseudoternary_levels = np.append(pseudoternary_levels, pseudoternary_levels[-1:])
    mlt3_levels = np.append(mlt3_levels, mlt3_levels[-1:])
    
    print([str(bit) for bit in bits], "Bits")
    print(nrzl_text, "NRZ-L")
    print(pseudoternary_text, "Pseudoternary")
    print(mlt3_text, "MLT-3")

    repeated_bits = np.repeat(bits, 2) # double sequence of bits to fill x axis
    x_coords = 0.5 * np.arange(len(repeated_bits)) # x coordinates, advance by .5
    x_coords = np.append(x_coords, x_coords[-1]+0.5) # add extra bit 0.5 greater than last in t

    # initalize graph with appropriate lines to plot schemes
    createAxes('x', range(len(bits)+1), color='.5', linewidth=2) 
    createAxes('y', [1, 5, 9, 13], color='.5', linewidth=2)

    # change o in plot.step to r,g,b (respectively) to get a graph without emphasized plot points
    # (x_coords, scheme+adjustement val to move up y-axis, color, line thickness, position, label)    
    plt.step(x_coords, nrzl_levels + 9, 'o', linewidth = 2, where='post', label='NRZ-L')
    plt.step(x_coords, pseudoternary_levels + 5, 'o', linewidth = 2, where='post', label='Pseudoternary')
    plt.step(x_coords, mlt3_levels + 1, 'o', linewidth = 2, where='post', label='MLT-3')
    plt.legend(loc='upper right', prop={'size': 10})
    plt.ylim([-2, 17])

    for x_coord, bit in enumerate(bits): # adds bit sequence above each scheme plot
        plt.text(x_coord + 0.5, 11, str(bit)) # (x, y, text)
        plt.text(x_coord + 0.5, 7, str(bit))
        plt.text(x_coord + 0.5, 3, str(bit))

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