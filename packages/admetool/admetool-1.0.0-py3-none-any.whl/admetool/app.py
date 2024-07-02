from models import *  # COLOCAR O PONTO DE VOLTA (.MODELS)
import json
import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Process some files with different tools.')

    subparsers = parser.add_subparsers(dest='tool', required=True, help='')

    # sdf
    parser_sdf = subparsers.add_parser('sdf', help='Process SDF files.')

    parser_sdf.add_argument('-i', '--input_file', type=str, required=True, help='Input SDF file')
    parser_sdf.add_argument('-db', '--database', type=str, required=True, help='Database name')
    parser_sdf.add_argument('-n', '--batch', type=int, default=299, help='Number of molecules per batch')
    parser_sdf.add_argument('-af', '--affinity', type=float, required=True, help='Affinity cutoff value')

    # score
    parser_score = subparsers.add_parser('score', help='Tool that creates an admet analysis spreadsheet, listing the best molecule options by score.')

    parser_score.add_argument('-i', '--input_file', type=str, required=True, help='Input file')
    parser_score.add_argument('-t', '--best_hits', type=int, default=10000, help='Best hits file')
    parser_score.add_argument('-s', '--sdf', type=str, required=True, help='SDF file')
    parser.add_argument('-w', '--weights',
                    type=str,
                    help='File to change weights in the AdmetLab spreadsheet analysis (.JSON)')

    args = parser.parse_args()
    weights = None
    if args.weights:
        with open(args.weights, "r", encoding="utf-8") as f:
            weights = json.loads(f.read())

    if args.tool == 'sdf':
        process_sdf(args.input_file, args.database, args.batch, args.affinity)

    elif args.tool == 'score':
        process_score(args.input_file, args.best_hits, args.sdf, args.weights)

def process_sdf(input_file, database, batch, affinity):

    sdf_instance = Sdf()

    sdf_instance.process_sdf(input_file, database, batch, affinity)

def process_score(input_file, best_hits, sdf, weights):

    extract_instance = Extract()
    analysis_instance = AdmetSpreadsheet()
    spreadsheet_instance = Spreadsheet()

    df = extract_instance.extract(input_file, sdf)
    df = analysis_instance.process_data(df, weights)
    spreadsheet_instance.spreadsheet_output(df, best_hits)

if __name__ == '__main__':
    main()
