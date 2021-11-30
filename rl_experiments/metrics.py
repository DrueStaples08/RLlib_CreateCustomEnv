import matplotlib.pyplot as plt

def visualize(reward_mean, length_mean, reward_max, reward_min):
    # Visualize Results
    fig, axs = plt.subplots(2,2)



    axs[0,0].plot(range(1, len(reward_mean)+1), reward_mean)
    axs[0,0].set_title('Mean Reward')

    axs[0,1].plot(range(1, len(length_mean)+1), length_mean)
    axs[0,1].set_title('Mean Episode Length')

    axs[1,0].plot(range(1, len(reward_max)+1), reward_max)
    axs[1,0].set_title('Max Reward')

    axs[1,1].plot(range(1, len(reward_min)+1), reward_min)
    axs[1,1].set_title('Min Reward')

    plt.suptitle('Chain Environment')
    fig.tight_layout(pad=0.3)
    plt.savefig('nchain.png', facecolor='white')
    plt.show()