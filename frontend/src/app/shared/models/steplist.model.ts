import { Step } from './step.model';

export class StepList {
  constructor(public name: string, public totaltime: number,
    public preptime: number, public cooktime: number,
    public displayorder: number, public steps: Step[]) { }
}
