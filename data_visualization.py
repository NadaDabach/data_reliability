import os
import matplotlib.pyplot as plt


def visualize_store_daily_visits(data, save_dir=None):
    """
    Visualize the store daily visits.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['visits_date'], data['store_daily_visits'], marker='o', linestyle='-')
    plt.title('Store Daily Visits')
    plt.xlabel('Date')
    plt.ylabel('Number of Visits')
    plt.tight_layout()
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, 'store_daily_visits.png'))
    plt.show()


def visualize_gender_repartition(data, save_dir=None):
    """
    Visualize the gender repartition in the store daily visits.
    """
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', stacked=True, colormap='cividis')
    plt.xlabel('Date')
    plt.ylabel('Number of Visits')
    plt.title('Gender Repartition in Store Daily Visits')
    plt.xticks(rotation=45)
    plt.legend(title='Gender')
    plt.tight_layout()
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, 'gender_repartition.png'))
    plt.show()


def visualize_age_proportions(data, save_dir=None):
    """
    Visualize the proportion of young, adult, and older people in the store daily visits
    using area plot
    """
    plt.figure(figsize=(10, 6))
    data.plot(kind='area', stacked=True, colormap='cividis')
    plt.xlabel('Date')
    plt.ylabel('Age Proportion')
    plt.title('Proportion of Young, Adult, and Older People in the Store Daily Visits')
    plt.xticks(rotation=45)
    plt.legend(title='Age')
    plt.tight_layout()
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, 'age_proportion.png'))
    plt.show()