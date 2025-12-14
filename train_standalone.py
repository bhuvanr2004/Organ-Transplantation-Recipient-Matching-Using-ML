#!/usr/bin/env python3
"""
Standalone script to train the OrganMatch ML model
"""

import pandas as pd
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.train_model import train_model

def main():
    print("🚀 Starting OrganMatch Model Training")
    print("=" * 50)

    # Load sample data
    try:
        print("📥 Loading donor and recipient data...")
        donors_df = pd.read_csv('data/donors_sample.csv')
        recipients_df = pd.read_csv('data/recipients_sample.csv')

        print(f"✅ Loaded {len(donors_df)} donors and {len(recipients_df)} recipients")

    except FileNotFoundError as e:
        print(f"❌ Error: Could not find sample data files: {e}")
        print("   Make sure data/donors_sample.csv and data/recipients_sample.csv exist")
        return 1
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return 1

    # Train the model
    try:
        print("\n🤖 Training ML model...")
        model = train_model(donors_df, recipients_df)

        if model is None:
            print("❌ Model training failed")
            return 1

        print("\n🎉 Model training completed successfully!")
        print("📁 Model saved to: models/random_forest.joblib")

    except Exception as e:
        print(f"❌ Error during training: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)